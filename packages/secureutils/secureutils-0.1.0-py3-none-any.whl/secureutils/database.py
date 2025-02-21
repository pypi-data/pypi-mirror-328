"""
SQLite database wrapper with connection pooling and query builder.
"""

import sqlite3
from typing import Any, Dict, List, Optional, Union, Tuple
import logging
from contextlib import contextmanager
from queue import Queue, Empty
import threading
import time

logger = logging.getLogger(__name__)

class ConnectionPool:
    def __init__(self, database: str, max_connections: int = 5):
        """
        Initialize connection pool.

        Args:
            database: Database file path
            max_connections: Maximum number of connections in pool
        """
        self.database = database
        self.max_connections = max_connections
        self.pool = Queue(maxsize=max_connections)
        self.lock = threading.Lock()
        self.active_connections = 0
        self._initialize_pool()

    def _create_connection(self) -> sqlite3.Connection:
        """Create a new SQLite connection with proper settings."""
        conn = sqlite3.connect(self.database, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _initialize_pool(self):
        """Initialize the connection pool with SQLite connections."""
        try:
            with self.lock:
                for _ in range(self.max_connections):
                    conn = self._create_connection()
                    self.pool.put(conn)
                    self.active_connections += 1
        except Exception as e:
            logger.error(f"Failed to initialize connection pool: {str(e)}")
            raise

    def _validate_connection(self, conn: sqlite3.Connection) -> bool:
        """Validate if a connection is still usable."""
        try:
            conn.execute("SELECT 1").fetchone()
            return True
        except (sqlite3.Error, Exception):
            return False

    @contextmanager
    def get_connection(self):
        """Context manager for getting a connection from the pool."""
        connection = None
        try:
            # Try to get a connection with timeout
            connection = self.pool.get(timeout=5)

            # Validate the connection
            if not self._validate_connection(connection):
                logger.warning("Invalid connection detected, creating new one")
                connection.close()
                connection = self._create_connection()

            yield connection
        except Empty:
            logger.error("Timeout waiting for available database connection")
            raise TimeoutError("No available database connections")
        except Exception as e:
            logger.error(f"Error getting connection from pool: {str(e)}")
            raise
        finally:
            if connection:
                try:
                    # Return connection to pool if it's still valid
                    if self._validate_connection(connection):
                        self.pool.put(connection)
                    else:
                        with self.lock:
                            self.active_connections -= 1
                            if self.active_connections < self.max_connections:
                                new_conn = self._create_connection()
                                self.pool.put(new_conn)
                                self.active_connections += 1
                except Exception as e:
                    logger.error(f"Error returning connection to pool: {str(e)}")
                    try:
                        connection.close()
                    except Exception:
                        pass

    def close_all(self):
        """Close all connections in the pool."""
        with self.lock:
            while not self.pool.empty():
                try:
                    conn = self.pool.get_nowait()
                    conn.close()
                    self.active_connections -= 1
                except Exception as e:
                    logger.error(f"Error closing connection: {str(e)}")

class DatabaseManager:
    def __init__(self, database: str):
        """
        Initialize DatabaseManager.

        Args:
            database: Database file path
        """
        self.pool = ConnectionPool(database)

    def execute(
        self,
        query: str,
        parameters: Optional[Union[Tuple[Any, ...], Dict[str, Any]]] = None
    ) -> sqlite3.Cursor:
        """
        Execute a SQL query.

        Args:
            query: SQL query string
            parameters: Query parameters

        Returns:
            Cursor: Query cursor
        """
        with self.pool.get_connection() as conn:
            try:
                cursor = conn.cursor()
                if parameters:
                    cursor.execute(query, parameters)
                else:
                    cursor.execute(query)
                conn.commit()
                return cursor
            except sqlite3.Error as e:
                conn.rollback()
                logger.error(f"SQL error: {str(e)}, Query: {query}")
                raise
            except Exception as e:
                conn.rollback()
                logger.error(f"Query execution failed: {str(e)}")
                raise

    def _row_to_dict(self, cursor: sqlite3.Cursor, row: sqlite3.Row) -> Dict[str, Any]:
        """Convert a database row to a dictionary."""
        if row is None:
            return {}
        return dict(zip([d[0] for d in cursor.description], tuple(row)))

    def fetch_one(
        self,
        query: str,
        parameters: Optional[Union[Tuple[Any, ...], Dict[str, Any]]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Fetch a single row from the database.

        Args:
            query: SQL query string
            parameters: Query parameters

        Returns:
            Optional[Dict[str, Any]]: Single row as dictionary or None
        """
        try:
            cursor = self.execute(query, parameters)
            row = cursor.fetchone()
            if row is None:
                return None
            return self._row_to_dict(cursor, row)
        except Exception as e:
            logger.error(f"Failed to fetch row: {str(e)}")
            return None

    def fetch_all(
        self,
        query: str,
        parameters: Optional[Union[Tuple[Any, ...], Dict[str, Any]]] = None
    ) -> List[Dict[str, Any]]:
        """
        Fetch all rows from the database.

        Args:
            query: SQL query string
            parameters: Query parameters

        Returns:
            List[Dict[str, Any]]: List of rows as dictionaries
        """
        try:
            cursor = self.execute(query, parameters)
            return [self._row_to_dict(cursor, row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to fetch rows: {str(e)}")
            return []

    def create_table(self, table_name: str, columns: Dict[str, str]):
        """
        Create a new table.

        Args:
            table_name: Name of the table
            columns: Dictionary of column names and their types
        """
        columns_def = ", ".join(f"{name} {type_}" for name, type_ in columns.items())
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        self.execute(query)

    def insert(self, table_name: str, data: Dict[str, Any]):
        """
        Insert data into a table.

        Args:
            table_name: Name of the table
            data: Dictionary of column names and values
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute(query, tuple(data.values()))

    def close(self):
        """Close all database connections."""
        self.pool.close_all()