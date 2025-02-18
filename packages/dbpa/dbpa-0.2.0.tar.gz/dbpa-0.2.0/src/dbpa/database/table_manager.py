"""Table management functionality for DBPA."""

from typing import List, Dict, Optional
import pandas as pd
from pathlib import Path

from dbpa.database.database_connection import DatabaseConnection
from dbpa.utils.error_logger import ErrorLogger


class TableManager:
    """Manages database table operations and metadata."""

    def __init__(self) -> None:
        """Initialize the TableManager."""
        self.db = DatabaseConnection()
        self.error_logger = ErrorLogger()
        self.selected_tables: List[str] = []

    def get_available_tables(self) -> List[str]:
        """Get list of available tables in the database.
        
        Returns:
            List[str]: List of table names
        """
        try:
            query = """
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """
            result = self.db.execute_query(query)
            return [row[0] for row in result]
        except Exception as e:
            self.error_logger.log_error(f"Error getting available tables: {str(e)}")
            return []

    def get_table_details(self, table_name: str) -> pd.DataFrame:
        """Get detailed information about a specific table.
        
        Args:
            table_name: Name of the table
            
        Returns:
            pd.DataFrame: Table column information
        """
        try:
            query = """
                SELECT 
                    column_name,
                    data_type,
                    is_nullable,
                    column_default,
                    character_maximum_length
                FROM information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position;
            """
            result = self.db.execute_query(query, (table_name,))
            return pd.DataFrame(
                result,
                columns=[
                    "Column Name",
                    "Data Type",
                    "Nullable",
                    "Default",
                    "Max Length"
                ]
            )
        except Exception as e:
            self.error_logger.log_error(
                f"Error getting table details for {table_name}: {str(e)}"
            )
            return pd.DataFrame()

    def get_row_count(self, table_name: str) -> int:
        """Get the number of rows in a table.
        
        Args:
            table_name: Name of the table
            
        Returns:
            int: Number of rows
        """
        try:
            query = f"SELECT COUNT(*) FROM {table_name};"
            result = self.db.execute_query(query)
            return result[0][0] if result else 0
        except Exception as e:
            self.error_logger.log_error(
                f"Error getting row count for {table_name}: {str(e)}"
            )
            return 0

    def get_sample_data(
        self, table_name: str, limit: int = 5
    ) -> pd.DataFrame:
        """Get sample data from a table.
        
        Args:
            table_name: Name of the table
            limit: Maximum number of rows to return
            
        Returns:
            pd.DataFrame: Sample data
        """
        try:
            query = f"SELECT * FROM {table_name} LIMIT {limit};"
            result = self.db.execute_query(query)
            columns = [
                desc[0] 
                for desc in self.db.cursor.description
            ] if self.db.cursor else []
            return pd.DataFrame(result, columns=columns)
        except Exception as e:
            self.error_logger.log_error(
                f"Error getting sample data for {table_name}: {str(e)}"
            )
            return pd.DataFrame()

    def get_table_relationships(self, table_name: str) -> List[str]:
        """Get foreign key relationships for a table.
        
        Args:
            table_name: Name of the table
            
        Returns:
            List[str]: List of relationship descriptions
        """
        try:
            query = """
                SELECT
                    tc.table_schema, 
                    tc.constraint_name, 
                    tc.table_name, 
                    kcu.column_name,
                    ccu.table_schema AS foreign_table_schema,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM 
                    information_schema.table_constraints AS tc 
                    JOIN information_schema.key_column_usage AS kcu
                      ON tc.constraint_name = kcu.constraint_name
                      AND tc.table_schema = kcu.table_schema
                    JOIN information_schema.constraint_column_usage AS ccu
                      ON ccu.constraint_name = tc.constraint_name
                      AND ccu.table_schema = tc.table_schema
                WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name=%s;
            """
            result = self.db.execute_query(query, (table_name,))
            relationships = []
            for row in result:
                rel = (
                    f"{row[2]}.{row[3]} -> "
                    f"{row[5]}.{row[6]}"
                )
                relationships.append(rel)
            return relationships
        except Exception as e:
            self.error_logger.log_error(
                f"Error getting relationships for {table_name}: {str(e)}"
            )
            return []
