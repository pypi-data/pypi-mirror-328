import json
import os
import urllib.parse
from dataclasses import dataclass, field
from logging import getLogger
from typing import Optional, Dict

from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.engine import URL
from sqlalchemy.engine.base import Engine

_log = getLogger(__name__)


class DatabaseConnectionError(Exception):
    """Custom exception for database connection errors."""
    pass


@dataclass
class ConnectionConfig:
    dsName: str
    dsType: int
    schema: str = "public"
    workspaceName: str = "default"
    table: Optional[str] = None
    host: Optional[str] = None
    magicToken: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    instanceName: Optional[str] = None
    options: Dict[str, str] = field(default_factory=dict)
    query: Dict[str, str] = field(default_factory=dict)


class DatabaseConnectionManager:
    """
    Manages database connections with flexible configuration options.
    """

    def __init__(self, ds_name: Optional[str] = None):
        """
        Initialize a database connection for a specific data source.
        """
        self._ds_name = ds_name
        self._vcluster: Optional[str] = None
        self._workspace: Optional[str] = None
        self._driver: Optional[str] = None
        self._schema: Optional[str] = None
        self._engine: Optional[Engine] = None
        self._options = {}
        self._query: Dict[str, str] = {}
        self._host: Optional[str] = None

    @classmethod
    def load_connection_configs(cls) -> Dict[str, ConnectionConfig]:
        """
        Load and cache connection configurations from environment variables.

        Returns:
            Dict of connection configurations keyed by data source name
        """
        if not hasattr(DatabaseConnectionManager, '_connection_cache'):
            # Retrieve and decode connection info from environment variable
            conn_info_str = None
            if name := os.environ.get('EXECUTE_LOG_ID'):
                pipe_path = '/tmp/' + name
                try:
                    pipe_fd = os.open(pipe_path, os.O_RDONLY)
                    with os.fdopen(pipe_fd, 'r') as pipe:
                        conn_info_str = pipe.read()
                except FileNotFoundError:
                    pass
            # Fall back to environment variable if pipe is not found
            conn_info_str = conn_info_str or os.environ.get('connectionInfos', '[]')
            if not conn_info_str:
                raise DatabaseConnectionError("No connection information found in env")
            decoded_info = urllib.parse.unquote(conn_info_str)
            conn_list = json.loads(decoded_info)

            # Create connection configs
            cls._connection_cache = {
                info.get('dsName'): ConnectionConfig(**info)
                for info in conn_list
            }

        return cls._connection_cache

    def get_connection_info(self, ds_name: str) -> ConnectionConfig:
        """
        Find connection info by data source name
        """
        connections = self.load_connection_configs()

        # Validate data source exists
        if ds_name not in connections:
            raise DatabaseConnectionError(f"Data source '{ds_name}' not found")

        config = connections.get(ds_name)
        config.options.update(self._options)
        if self._query:
            config.query.update(self._query)
        return config

    @classmethod
    def get_connection_infos(cls) -> Dict[str, ConnectionConfig]:
        """
        Get all connection infos
        """
        return DatabaseConnectionManager.load_connection_configs()

    def use_workspace(self, workspace: str) -> 'DatabaseConnectionManager':
        """
        Set workspace for the connection.

        Args:
            workspace (str): Workspace name

        Returns:
            self: For method chaining
        """
        self._workspace = workspace
        return self

    def use_driver(self, driver: str) -> 'DatabaseConnectionManager':
        """
        Set driver for the connection.

        Args:
            driver (str): Driver name

        Returns:
            self: For method chaining
        """
        self._driver = driver
        return self

    def use_schema(self, schema: str) -> 'DatabaseConnectionManager':
        """
        Set schema for the connection.

        Args:
            schema (str): Schema name

        Returns:
            self: For method chaining
        """
        self._schema = schema
        return self

    def use_vcluster(self, vcluster: str) -> 'DatabaseConnectionManager':
        """
        Set virtual cluster for the connection.

        Args:
            vcluster (str): Virtual cluster name

        Returns:
            self: For method chaining
        """
        self._vcluster = vcluster
        return self

    def use_options(self, options):
        """
        Set additional connection options.

        Args:
            options (dict): Additional connection options

        Returns:
            self: For method chaining
        """
        if options:
            self._options.update(options)
        return self

    def use_query(self, query: dict) -> 'DatabaseConnectionManager':
        """
        Set query for the connection.
        Args:
            query (str): Query string
        Returns:
            self: For method chaining
        """
        if query:
            self._query.update(query)
        return self

    def use_host(self, host: str) -> 'DatabaseConnectionManager':
        """
        Set host for the connection.
        Args:
            host (str): Host name
        Returns:
            self: For method chaining
        """
        if host:
            self._host = host
        return self

    def build(self, *args, **kwargs) -> Engine:
        """
        Create SQLAlchemy engine based on data source name and optional schema

        :return: SQLAlchemy Engine
        """
        conn_info: ConnectionConfig = self.get_connection_info(self._ds_name)

        if not conn_info.host:
            raise DatabaseConnectionError("Missing connection host for MySQL data source")

        ds_type = conn_info.dsType
        options = conn_info.options or {}
        schema = self._schema or conn_info.schema
        host = self._host or conn_info.host
        host_parts = host.split(':')
        connect_args = {}

        # Construct connection URL based on data source type
        if ds_type == 5:  # Mysql
            if not conn_info.username or not conn_info.password:
                raise DatabaseConnectionError("Missing username or password for MySQL data source")

            options.update(conn_info.query)
            url = URL.create(
                drivername=self._driver or 'mysql+mysqlconnector',
                username=conn_info.username,
                password=conn_info.password,
                host=host_parts[0],
                port=host_parts[1] if len(host_parts) > 1 else None,
                database=schema,
                query=options
            )
            return sa_create_engine(url, *args, **kwargs)

        elif ds_type == 7:  # PostgreSQL
            url = URL.create(
                drivername=self._driver or 'postgresql+psycopg2',
                username=conn_info.username,
                password=conn_info.password,
                host=host_parts[0],
                port=host_parts[1] if len(host_parts) > 1 else None,
                database=schema,
                query=conn_info.query
            )
            connect_args = {'options': self._convert_options(options)}

        elif ds_type == 1:  # ClickZetta
            if not conn_info.workspaceName or not conn_info.instanceName:
                raise DatabaseConnectionError("Missing required parameters 'workspace_name', "
                                              "'instance_name' for ClickZetta data source")
            if not self._vcluster:
                raise DatabaseConnectionError("Missing virtual cluster for ClickZetta data source")

            # Generate base parameters
            query_params = {
                "virtualcluster": self._vcluster
            }

            if schema:
                query_params["schema"] = schema

            query_params.update(options)
            query_params.update(conn_info.query)

            full_host = f"{conn_info.instanceName}.{conn_info.host}"

            if conn_info.username and conn_info.password:
                url = URL.create(
                    drivername="clickzetta",
                    username=conn_info.username,
                    password=conn_info.password,
                    host=full_host,
                    database=conn_info.workspaceName,
                    query=query_params
                )
            elif conn_info.magicToken:
                # Use magic token for authentication, do not require username and password
                query_params["magic_token"] = conn_info.magicToken
                url = URL.create(
                    drivername="clickzetta",
                    host=full_host,
                    database=conn_info.workspaceName,
                    query=query_params
                )
            else:
                raise ValueError("username and password or token must be specified")
        else:
            raise ValueError(f"Unsupported data source type: {ds_type}")

        self._engine = sa_create_engine(url, connect_args=connect_args, *args, **kwargs)
        return self._engine

    @staticmethod
    def _convert_options(options):
        if not options:
            return ''
        return ' '.join([f'-c{k}={v}' for k, v in options.items()])


def get_lakehouse_connection(conn):
    return conn.connection.connection


def get_active_engine(
        ds_name: str,
        vcluster: Optional[str] = None,
        workspace: Optional[str] = None,
        schema: Optional[str] = None,
        options: Optional[Dict[str, str]] = None,
        query: Optional[Dict[str, str]] = None,
        driver: Optional[str] = None,
        host: Optional[str] = None,
        *args, **kwargs
) -> Engine:
    """
    Convenience function to create a database engine.

    Args:
        ds_name (str): Data source name. Required.
        vcluster (str, optional): Virtual cluster name for ClickZetta data source. Required for ClickZetta.
        workspace (str, optional): Workspace name. Default is 'default'.
        schema (str, optional): Schema name for the connection. Default is 'public'.
        options (dict, optional): Additional connection options.
        query (dict, optional): Additional query parameters for SQLAlchemy url.
        driver (str, optional): Driver name for the connection.
        host (str, optional): Host name for the connection.
        *args: Additional arguments for SQLAlchemy engine.

    Returns:
        SQLAlchemy Engine instance
    """
    manager = DatabaseConnectionManager(ds_name)

    if workspace:
        manager.use_workspace(workspace)
    if schema:
        manager.use_schema(schema)
    if vcluster:
        manager.use_vcluster(vcluster)
    if options:
        manager.use_options(options)
    if query:
        manager.use_query(query)
    if driver:
        manager.use_driver(driver)
    if host:
        manager.use_host(host)

    return manager.build(*args, **kwargs)


def get_active_lakehouse_engine(
        vcluster: Optional[str] = None,
        workspace: Optional[str] = None,
        schema: Optional[str] = None,
        options: Optional[Dict[str, str]] = None,
        query: Optional[Dict[str, str]] = None,
        driver: Optional[str] = None,
        *args, **kwargs
) -> Engine:
    """
    Convenience function to create a database engine for lakehouse (ClickZetta) data source.
    
    Args:
        vcluster (str, optional): Virtual cluster name for ClickZetta data source. Required.
        workspace (str, optional): Workspace name. Default is 'default'.
        schema (str, optional): Schema name for the connection. Default is 'public'.
        options (dict, optional): Additional connection options.
        query (dict, optional): Additional query parameters for SQLAlchemy url.
        driver (str, optional): Driver name for the connection.
        *args: Additional arguments for SQLAlchemy engine.
        **kwargs: Additional keyword arguments for SQLAlchemy engine.

    Returns:
        SQLAlchemy Engine instance

    Raises:
        DatabaseConnectionError: If no lakehouse data source is found in the configuration.
    """
    # Get all connection configurations
    conn_infos = DatabaseConnectionManager.get_connection_infos()

    # Find the lakehouse (ClickZetta) data source
    lakehouse_ds = None
    for ds_name, conn_info in conn_infos.items():
        if conn_info.dsType == 1:  # ClickZetta type
            lakehouse_ds = ds_name
            break

    if not lakehouse_ds:
        raise DatabaseConnectionError("No lakehouse data source found in configuration")

    # Create engine using the found lakehouse data source
    return get_active_engine(
        ds_name=lakehouse_ds,
        vcluster=vcluster,
        workspace=workspace,
        schema=schema,
        options=options,
        query=query,
        driver=driver,
        *args, **kwargs
    )

def clean_connection_cache():
    """Clear connection cache before each test"""
    if hasattr(DatabaseConnectionManager, '_connection_cache'):
        delattr(DatabaseConnectionManager, '_connection_cache')