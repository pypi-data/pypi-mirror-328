"""Schema analyzer component for analyzing database structure."""
from typing import Dict, List, Any
import logging
from datetime import datetime
from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.engine import Engine

from dbpa.txt2sql.agents.base import BaseAgent
from dbpa.txt2sql.agents.schema.utils import generate_schema_hash

logger = logging.getLogger(__name__)


class SchemaAnalyzer(BaseAgent):
    """Component for analyzing database schemas."""

    def __init__(self, name: str = "SchemaAnalyzer"):
        """Initialize schema analyzer.
        
        Args:
            name: Component name
        """
        super().__init__(name)
        self._engines: Dict[str, Engine] = {}
        self._metadata: Dict[str, MetaData] = {}
        self._schema_cache: Dict[str, Dict[str, Any]] = {}

    def _do_initialize(self) -> None:
        """Initialize component resources."""
        pass

    def _do_cleanup(self) -> None:
        """Cleanup component resources."""
        for engine in self._engines.values():
            engine.dispose()
        self._engines.clear()
        self._metadata.clear()
        self._schema_cache.clear()

    def analyze_schema(self, connection_string: str) -> Dict[str, Any]:
        """Analyze database schema.
        
        Args:
            connection_string: Database connection string
            
        Returns:
            Schema analysis results
        """
        start_time = datetime.now()
        
        # Create or get engine
        if connection_string not in self._engines:
            self._engines[connection_string] = create_engine(connection_string)
            self._metadata[connection_string] = MetaData()
            
        engine = self._engines[connection_string]
        metadata = self._metadata[connection_string]
        
        # Reflect schema
        metadata.reflect(bind=engine)
        inspector = inspect(engine)
        
        # Analyze schema
        schema_info = self._analyze_tables(inspector)
        
        # Generate schema hash
        schema_hash = generate_schema_hash(schema_info)
        schema_info["hash"] = schema_hash
        
        # Cache schema info
        self._schema_cache[schema_hash] = schema_info
        
        # Record metrics
        duration = (datetime.now() - start_time).total_seconds()
        self._record_metric(
            "schema_analysis_duration",
            duration,
            {"schema_hash": schema_hash}
        )
        
        return schema_info

    def _analyze_tables(self, inspector: Any) -> Dict[str, Any]:
        """Analyze database tables.
        
        Args:
            inspector: SQLAlchemy inspector
            
        Returns:
            Table analysis results
        """
        schema_info = {
            "tables": {},
            "relationships": [],
            "indexes": {},
            "constraints": {}
        }
        
        for table_name in inspector.get_table_names():
            columns = self._analyze_columns(inspector, table_name)
            foreign_keys = self._analyze_foreign_keys(inspector, table_name)
            indexes = self._analyze_indexes(inspector, table_name)
            
            schema_info["tables"][table_name] = {
                "columns": columns,
                "foreign_keys": foreign_keys,
                "indexes": indexes
            }
            
            # Add relationships
            for fk in foreign_keys:
                schema_info["relationships"].append({
                    "from_table": table_name,
                    "to_table": fk["referred_table"],
                    "from_columns": fk["constrained_columns"],
                    "to_columns": fk["referred_columns"]
                })
                
        return schema_info

    def _analyze_columns(self, inspector: Any, table_name: str) -> List[Dict[str, Any]]:
        """Analyze table columns.
        
        Args:
            inspector: SQLAlchemy inspector
            table_name: Name of table to analyze
            
        Returns:
            Column analysis results
        """
        columns = []
        for column in inspector.get_columns(table_name):
            columns.append({
                "name": column["name"],
                "type": str(column["type"]),
                "nullable": column.get("nullable", True),
                "default": str(column.get("default", "None")),
                "primary_key": column.get("primary_key", False)
            })
        return columns

    def _analyze_foreign_keys(
        self,
        inspector: Any,
        table_name: str
    ) -> List[Dict[str, Any]]:
        """Analyze table foreign keys.
        
        Args:
            inspector: SQLAlchemy inspector
            table_name: Name of table to analyze
            
        Returns:
            Foreign key analysis results
        """
        foreign_keys = []
        for fk in inspector.get_foreign_keys(table_name):
            foreign_keys.append({
                "constrained_columns": fk["constrained_columns"],
                "referred_table": fk["referred_table"],
                "referred_columns": fk["referred_columns"]
            })
        return foreign_keys

    def _analyze_indexes(
        self,
        inspector: Any,
        table_name: str
    ) -> List[Dict[str, Any]]:
        """Analyze table indexes.
        
        Args:
            inspector: SQLAlchemy inspector
            table_name: Name of table to analyze
            
        Returns:
            Index analysis results
        """
        indexes = []
        for idx in inspector.get_indexes(table_name):
            indexes.append({
                "name": idx["name"],
                "columns": idx["column_names"],
                "unique": idx["unique"]
            })
        return indexes
