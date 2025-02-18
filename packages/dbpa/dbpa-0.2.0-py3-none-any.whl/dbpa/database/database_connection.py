"""Database connection management for DBPA."""

from typing import Any, List, Optional, Tuple, Union
import os
from pathlib import Path
import psycopg2
from psycopg2.extensions import connection, cursor
from dotenv import load_dotenv

from dbpa.utils.error_logger import ErrorLogger


class DatabaseConnection:
    """Manages database connections and query execution."""

    def __init__(self) -> None:
        """Initialize database connection."""
        self.error_logger = ErrorLogger()
        self._load_config()
        self.conn: Optional[connection] = None
        self.cursor: Optional[cursor] = None
        self._connect()

    def _load_config(self) -> None:
        """Load database configuration from environment variables."""
        env_path = Path(__file__).parent.parent.parent.parent / ".env"
        load_dotenv(env_path)
        
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = int(os.getenv("POSTGRES_PORT", "5432"))
        self.database = os.getenv("POSTGRES_DATABASE", "")
        self.user = os.getenv("POSTGRES_USER", "")
        self.password = os.getenv("POSTGRES_PASSWORD", "")

    def _connect(self) -> None:
        """Establish database connection."""
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            self.error_logger.log_error(f"Database connection error: {str(e)}")
            raise

    def execute_query(
        self, 
        query: str, 
        params: Optional[Union[Tuple[Any, ...], List[Any]]] = None
    ) -> List[Tuple[Any, ...]]:
        """Execute a SQL query and return results.
        
        Args:
            query: SQL query string
            params: Query parameters
            
        Returns:
            List[Tuple[Any, ...]]: Query results
        """
        try:
            if not self.conn or self.conn.closed:
                self._connect()
            
            if not self.cursor:
                raise Exception("No cursor available")
                
            self.cursor.execute(query, params)
            
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
            
            self.conn.commit()
            return []
            
        except Exception as e:
            if self.conn:
                self.conn.rollback()
            self.error_logger.log_error(f"Query execution error: {str(e)}")
            raise

    def close(self) -> None:
        """Close database connection."""
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            self.error_logger.log_error(f"Error closing connection: {str(e)}")

    def __del__(self) -> None:
        """Ensure connection is closed when object is deleted."""
        self.close()
