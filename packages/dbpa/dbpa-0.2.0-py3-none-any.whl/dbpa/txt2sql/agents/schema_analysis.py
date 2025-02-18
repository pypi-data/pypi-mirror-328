"""Schema analysis agent for understanding database structure."""
from typing import Dict, List, Optional, Any
import logging
from datetime import datetime
import hashlib
import json
from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.engine import Engine
from sqlalchemy.sql import text

from dbpa.txt2sql.agents.base import BaseAgent
from dbpa.txt2sql.models.agent_models import Change, Template, Suggestion
from dbpa.txt2sql.models.examples import QueryExample

logger = logging.getLogger(__name__)


class SchemaAnalysisAgent(BaseAgent):
    """Agent for analyzing database schemas and generating templates."""

    def __init__(
        self,
        name: str = "SchemaAnalysisAgent",
        template_path: Optional[str] = None
    ):
        """Initialize schema analysis agent.
        
        Args:
            name: Agent name
            template_path: Optional path to template file
        """
        super().__init__(name)
        self._template_path = template_path
        self._engines: Dict[str, Engine] = {}
        self._metadata: Dict[str, MetaData] = {}
        self._schema_cache: Dict[str, Dict[str, Any]] = {}
        self._template_cache: Dict[str, List[Template]] = {}

    def _do_initialize(self) -> None:
        """Initialize agent resources."""
        if self._template_path:
            self._load_templates()

    def _do_cleanup(self) -> None:
        """Cleanup agent resources."""
        for engine in self._engines.values():
            engine.dispose()
        self._engines.clear()
        self._metadata.clear()
        self._schema_cache.clear()
        self._template_cache.clear()

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
        schema_info = {
            "tables": {},
            "relationships": [],
            "indexes": {},
            "constraints": {}
        }
        
        # Analyze tables
        for table_name in inspector.get_table_names():
            columns = []
            for column in inspector.get_columns(table_name):
                columns.append({
                    "name": column["name"],
                    "type": str(column["type"]),
                    "nullable": column.get("nullable", True),
                    "default": str(column.get("default", "None")),
                    "primary_key": column.get("primary_key", False)
                })
                
            foreign_keys = []
            for fk in inspector.get_foreign_keys(table_name):
                foreign_keys.append({
                    "constrained_columns": fk["constrained_columns"],
                    "referred_table": fk["referred_table"],
                    "referred_columns": fk["referred_columns"]
                })
                
            indexes = []
            for idx in inspector.get_indexes(table_name):
                indexes.append({
                    "name": idx["name"],
                    "columns": idx["column_names"],
                    "unique": idx["unique"]
                })
                
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
                
        # Generate schema hash
        schema_hash = self._generate_schema_hash(schema_info)
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

    def generate_templates(self, schema_hash: str) -> List[QueryExample]:
        """Generate query templates for schema.
        
        Args:
            schema_hash: Schema hash
            
        Returns:
            List of query examples
        """
        if schema_hash not in self._schema_cache:
            raise ValueError(f"Schema hash {schema_hash} not found")
            
        schema_info = self._schema_cache[schema_hash]
        templates = []
        
        # Generate basic templates
        for table_name, table_info in schema_info["tables"].items():
            # SELECT all
            templates.append(
                QueryExample(
                    natural_query=f"Get all {table_name}",
                    sql_query=f"SELECT * FROM {table_name}",
                    language="en",
                    database_type="postgresql",
                    schema_hash=schema_hash,
                    metadata={"template_type": "select_all"}
                )
            )
            
            # SELECT with conditions
            for column in table_info["columns"]:
                templates.append(
                    QueryExample(
                        natural_query=f"Find {table_name} where {column['name']} equals value",
                        sql_query=f"SELECT * FROM {table_name} WHERE {column['name']} = :value",
                        language="en",
                        database_type="postgresql",
                        schema_hash=schema_hash,
                        metadata={
                            "template_type": "select_where",
                            "parameter": column['name']
                        }
                    )
                )
                
        # Generate join templates
        for rel in schema_info["relationships"]:
            from_table = rel["from_table"]
            to_table = rel["to_table"]
            join_cond = " AND ".join(
                f"{from_table}.{fc} = {to_table}.{tc}"
                for fc, tc in zip(rel["from_columns"], rel["to_columns"])
            )
            
            templates.append(
                QueryExample(
                    natural_query=f"Get {from_table} with their {to_table}",
                    sql_query=f"SELECT * FROM {from_table} JOIN {to_table} ON {join_cond}",
                    language="en",
                    database_type="postgresql",
                    schema_hash=schema_hash,
                    metadata={"template_type": "join"}
                )
            )
            
        return templates

    def detect_schema_changes(
        self,
        old_hash: str,
        new_hash: str
    ) -> List[Change]:
        """Detect changes between schema versions.
        
        Args:
            old_hash: Old schema hash
            new_hash: New schema hash
            
        Returns:
            List of detected changes
        """
        if old_hash not in self._schema_cache or new_hash not in self._schema_cache:
            raise ValueError("Schema hash not found")
            
        old_schema = self._schema_cache[old_hash]
        new_schema = self._schema_cache[new_hash]
        changes = []
        
        # Detect table changes
        old_tables = set(old_schema["tables"].keys())
        new_tables = set(new_schema["tables"].keys())
        
        for table in new_tables - old_tables:
            changes.append(Change(
                type="table_added",
                object=table,
                details=f"New table {table} added",
                impact=["Queries can now reference new table"]
            ))
            
        for table in old_tables - new_tables:
            changes.append(Change(
                type="table_removed",
                object=table,
                details=f"Table {table} removed",
                impact=["Queries referencing this table will fail"]
            ))
            
        # Detect column changes
        for table in old_tables & new_tables:
            old_cols = {
                c["name"]: c for c in old_schema["tables"][table]["columns"]
            }
            new_cols = {
                c["name"]: c for c in new_schema["tables"][table]["columns"]
            }
            
            for col in set(new_cols) - set(old_cols):
                changes.append(Change(
                    type="column_added",
                    object=f"{table}.{col}",
                    details=f"New column {col} added to {table}",
                    impact=["SELECT * queries will return new column"]
                ))
                
            for col in set(old_cols) - set(new_cols):
                changes.append(Change(
                    type="column_removed",
                    object=f"{table}.{col}",
                    details=f"Column {col} removed from {table}",
                    impact=[
                        "Queries referencing this column will fail",
                        "SELECT * queries will no longer return this column"
                    ]
                ))
                
            for col in set(old_cols) & set(new_cols):
                if old_cols[col]["type"] != new_cols[col]["type"]:
                    changes.append(Change(
                        type="column_type_changed",
                        object=f"{table}.{col}",
                        details=(
                            f"Column {col} type changed from "
                            f"{old_cols[col]['type']} to {new_cols[col]['type']}"
                        ),
                        impact=["Type conversion may be needed"]
                    ))
                    
        return changes

    def suggest_optimizations(self, schema_hash: str) -> List[Suggestion]:
        """Suggest schema optimizations.
        
        Args:
            schema_hash: Schema hash
            
        Returns:
            List of optimization suggestions
        """
        if schema_hash not in self._schema_cache:
            raise ValueError(f"Schema hash {schema_hash} not found")
            
        schema_info = self._schema_cache[schema_hash]
        suggestions = []
        
        # Check for missing indexes on foreign keys
        for table_name, table_info in schema_info["tables"].items():
            existing_indexes = {
                tuple(sorted(idx["columns"]))
                for idx in table_info["indexes"]
            }
            
            for fk in table_info["foreign_keys"]:
                fk_cols = tuple(sorted(fk["constrained_columns"]))
                if fk_cols not in existing_indexes:
                    suggestions.append(Suggestion(
                        category="missing_index",
                        description=f"Missing index on foreign key columns in {table_name}",
                        current="No index on foreign key columns",
                        proposed=f"CREATE INDEX ON {table_name} ({', '.join(fk_cols)})",
                        benefit="Improve JOIN performance"
                    ))
                    
        # Check for tables without primary keys
        for table_name, table_info in schema_info["tables"].items():
            has_pk = any(col["primary_key"] for col in table_info["columns"])
            if not has_pk:
                suggestions.append(Suggestion(
                    category="missing_primary_key",
                    description=f"Table {table_name} has no primary key",
                    current="No primary key defined",
                    proposed="Add a primary key constraint",
                    benefit="Ensure data integrity and improve query performance"
                ))
                
        return suggestions

    def _generate_schema_hash(self, schema_info: Dict[str, Any]) -> str:
        """Generate hash for schema.
        
        Args:
            schema_info: Schema information
            
        Returns:
            Schema hash
        """
        # Create a deterministic string representation
        schema_str = json.dumps(schema_info, sort_keys=True)
        return hashlib.sha256(schema_str.encode()).hexdigest()

    def _load_templates(self) -> None:
        """Load templates from file."""
        try:
            with open(self._template_path, 'r') as f:
                templates_data = json.load(f)
                
            for schema_hash, templates in templates_data.items():
                self._template_cache[schema_hash] = [
                    Template(**t) for t in templates
                ]
                
            logger.info(f"Loaded {len(templates_data)} template sets")
        except Exception as e:
            logger.error(f"Failed to load templates: {str(e)}")
            raise
