"""Template generator for schema-based queries."""
from typing import Dict, List, Any
import logging
import json
from pathlib import Path

from dbpa.txt2sql.models.agent_models import Template
from dbpa.txt2sql.models.examples import QueryExample
from dbpa.txt2sql.agents.base import BaseAgent

logger = logging.getLogger(__name__)


class TemplateGenerator(BaseAgent):
    """Component for generating query templates."""

    def __init__(
        self,
        name: str = "TemplateGenerator",
        template_path: Path = None
    ):
        """Initialize template generator.
        
        Args:
            name: Component name
            template_path: Optional path to template file
        """
        super().__init__(name)
        self._template_path = template_path
        self._template_cache: Dict[str, List[Template]] = {}

    def _do_initialize(self) -> None:
        """Initialize component resources."""
        if self._template_path:
            self._load_templates()

    def _do_cleanup(self) -> None:
        """Cleanup component resources."""
        self._template_cache.clear()

    def generate_templates(
        self,
        schema_info: Dict[str, Any],
        schema_hash: str
    ) -> List[QueryExample]:
        """Generate query templates for schema.
        
        Args:
            schema_info: Schema information
            schema_hash: Schema hash
            
        Returns:
            List of query examples
        """
        templates = []
        
        # Generate basic templates
        templates.extend(self._generate_basic_templates(schema_info, schema_hash))
        
        # Generate join templates
        templates.extend(self._generate_join_templates(schema_info, schema_hash))
        
        # Add cached templates if available
        if schema_hash in self._template_cache:
            templates.extend(
                self._convert_template_to_example(t, schema_hash)
                for t in self._template_cache[schema_hash]
            )
            
        return templates

    def _generate_basic_templates(
        self,
        schema_info: Dict[str, Any],
        schema_hash: str
    ) -> List[QueryExample]:
        """Generate basic query templates.
        
        Args:
            schema_info: Schema information
            schema_hash: Schema hash
            
        Returns:
            List of basic query examples
        """
        templates = []
        
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
                
        return templates

    def _generate_join_templates(
        self,
        schema_info: Dict[str, Any],
        schema_hash: str
    ) -> List[QueryExample]:
        """Generate join query templates.
        
        Args:
            schema_info: Schema information
            schema_hash: Schema hash
            
        Returns:
            List of join query examples
        """
        templates = []
        
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

    def _convert_template_to_example(
        self,
        template: Template,
        schema_hash: str
    ) -> QueryExample:
        """Convert template to query example.
        
        Args:
            template: Template to convert
            schema_hash: Schema hash
            
        Returns:
            Query example
        """
        return QueryExample(
            natural_query=template.natural_template,
            sql_query=template.sql_template,
            language="en",
            database_type="postgresql",
            schema_hash=schema_hash,
            metadata={
                "template_type": "custom",
                "template_name": template.name,
                **template.metadata
            }
        )

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
