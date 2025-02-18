"""Text to SQL conversion engine with advanced features."""
from typing import Dict, List, Optional, Union, Any
from pydantic import BaseModel
from dbpa.config.config_schema import DatabaseConfig, ProjectConfig
import sqlalchemy as sa
from sqlalchemy import inspect
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI, Groq
import logging

logger = logging.getLogger(__name__)

class TableMetadata(BaseModel):
    """Table metadata for schema understanding."""
    name: str
    schema: Optional[str]
    columns: List[Dict[str, Any]]
    primary_keys: List[str]
    foreign_keys: List[Dict[str, str]]
    indexes: List[Dict[str, Any]]
    sample_data: Optional[pd.DataFrame]


class DatabaseContext(BaseModel):
    """Database context for query generation."""
    tables: Dict[str, TableMetadata]
    relationships: List[Dict[str, Any]]
    common_queries: List[Dict[str, str]]
    constraints: List[Dict[str, Any]]


class QueryResult(BaseModel):
    """Result of a query execution."""
    sql: str
    success: bool
    error: Optional[str]
    data: Optional[pd.DataFrame]
    execution_time: float
    affected_rows: Optional[int]


class Txt2SQLEngine:
    """Text to SQL conversion engine."""
    
    def __init__(
        self,
        db_config: DatabaseConfig,
        project_config: ProjectConfig,
        llm_config: Any
    ):
        """Initialize the engine."""
        self.db_config = db_config
        self.project_config = project_config
        self.llm_config = llm_config
        self.engine = self._create_engine()
        self.db_context = self._build_database_context()
        self.llm_chain = self._setup_llm_chain()

    def _create_engine(self) -> sa.engine.Engine:
        """Create SQLAlchemy engine."""
        if self.db_config.connection_string:
            return sa.create_engine(self.db_config.connection_string)
        
        url = sa.URL.create(
            drivername=f"{self.db_config.type}+psycopg2",
            username=self.db_config.username,
            password=self.db_config.password,
            host=self.db_config.host,
            port=self.db_config.port,
            database=self.db_config.database
        )
        return sa.create_engine(url)

    def _build_database_context(self) -> DatabaseContext:
        """Build database context from schema."""
        inspector = inspect(self.engine)
        tables = {}
        relationships = []

        for schema in inspector.get_schema_names():
            if schema in ('information_schema', 'pg_catalog'):
                continue

            for table_name in inspector.get_table_names(schema=schema):
                table_info = TableMetadata(
                    name=table_name,
                    schema=schema,
                    columns=inspector.get_columns(table_name, schema),
                    primary_keys=inspector.get_pk_constraint(table_name, schema)['constrained_columns'],
                    foreign_keys=[{
                        'column': fk['constrained_columns'][0],
                        'references': f"{fk['referred_table']}.{fk['referred_columns'][0]}"
                    } for fk in inspector.get_foreign_keys(table_name, schema)],
                    indexes=inspector.get_indexes(table_name, schema)
                )
                
                # Get sample data
                try:
                    sample_query = f"SELECT * FROM {schema}.{table_name} LIMIT 5"
                    table_info.sample_data = pd.read_sql(sample_query, self.engine)
                except Exception as e:
                    logger.warning(f"Could not get sample data for {schema}.{table_name}: {e}")

                tables[f"{schema}.{table_name}"] = table_info

                # Build relationships
                for fk in table_info.foreign_keys:
                    relationships.append({
                        'from_table': f"{schema}.{table_name}",
                        'from_column': fk['column'],
                        'to_table': fk['references'].split('.')[0],
                        'to_column': fk['references'].split('.')[1]
                    })

        return DatabaseContext(
            tables=tables,
            relationships=relationships,
            common_queries=self._load_common_queries(),
            constraints=self._load_constraints()
        )

    def _load_common_queries(self) -> List[Dict[str, str]]:
        """Load common query patterns."""
        return [
            {
                'name': 'count_records',
                'pattern': 'SELECT COUNT(*) FROM {table}',
                'description': 'Count total records in a table'
            },
            {
                'name': 'latest_records',
                'pattern': 'SELECT * FROM {table} ORDER BY {timestamp_column} DESC LIMIT {limit}',
                'description': 'Get latest records from a table'
            },
            # Add more common query patterns
        ]

    def _load_constraints(self) -> List[Dict[str, Any]]:
        """Load database constraints."""
        constraints = []
        for table_name in self.db_context.tables:
            schema, table = table_name.split('.')
            for constraint in inspect(self.engine).get_check_constraints(table, schema):
                constraints.append({
                    'table': table_name,
                    'name': constraint['name'],
                    'sqltext': constraint['sqltext']
                })
        return constraints

    def _setup_llm_chain(self) -> LLMChain:
        """Setup LLM chain for query generation."""
        prompt = PromptTemplate(
            template="""Given the following database context and natural language query, 
            generate a SQL query that answers the question.

            Database Context:
            {db_context}

            Question: {question}

            Rules:
            1. Use proper table schema prefixes
            2. Include appropriate JOINs based on relationships
            3. Handle NULL values appropriately
            4. Use column names exactly as they appear in schema
            5. Add comments for complex parts of the query

            SQL Query:""",
            input_variables=["db_context", "question"]
        )

        if self.llm_config.provider == "openai":
            llm = OpenAI(
                api_key=self.llm_config.api_key,
                model=self.llm_config.model,
                temperature=self.llm_config.temperature
            )
        elif self.llm_config.provider == "groq":
            llm = Groq(
                api_key=self.llm_config.api_key,
                model=self.llm_config.model
            )
        else:
            raise ValueError(f"Unsupported LLM provider: {self.llm_config.provider}")

        return LLMChain(llm=llm, prompt=prompt)

    def generate_query(self, question: str) -> str:
        """Generate SQL query from natural language."""
        db_context_str = self._format_db_context()
        return self.llm_chain.predict(
            db_context=db_context_str,
            question=question
        )

    def _format_db_context(self) -> str:
        """Format database context for LLM."""
        context = []
        
        # Tables and columns
        context.append("Tables:")
        for table_name, table in self.db_context.tables.items():
            context.append(f"\n{table_name}:")
            for col in table.columns:
                context.append(f"  - {col['name']}: {col['type']}")

        # Relationships
        context.append("\nRelationships:")
        for rel in self.db_context.relationships:
            context.append(
                f"  - {rel['from_table']}.{rel['from_column']} -> "
                f"{rel['to_table']}.{rel['to_column']}"
            )

        # Constraints
        context.append("\nConstraints:")
        for constraint in self.db_context.constraints:
            context.append(
                f"  - {constraint['table']}: {constraint['sqltext']}"
            )

        return "\n".join(context)

    def execute_query(self, sql: str) -> QueryResult:
        """Execute a SQL query and return results."""
        import time
        start_time = time.time()
        
        try:
            if sql.lower().startswith(('select', 'with')):
                df = pd.read_sql(sql, self.engine)
                affected_rows = len(df)
            else:
                with self.engine.begin() as conn:
                    result = conn.execute(sa.text(sql))
                    affected_rows = result.rowcount
                    df = None

            return QueryResult(
                sql=sql,
                success=True,
                error=None,
                data=df,
                execution_time=time.time() - start_time,
                affected_rows=affected_rows
            )

        except Exception as e:
            return QueryResult(
                sql=sql,
                success=False,
                error=str(e),
                data=None,
                execution_time=time.time() - start_time,
                affected_rows=None
            )

    def explain_query(self, sql: str) -> str:
        """Explain the execution plan of a query."""
        try:
            with self.engine.connect() as conn:
                if self.db_config.type == "postgresql":
                    result = conn.execute(sa.text(f"EXPLAIN ANALYZE {sql}"))
                    return "\n".join([row[0] for row in result])
                # Add support for other databases' EXPLAIN syntax
                return "Query explanation not supported for this database type"
        except Exception as e:
            return f"Error explaining query: {str(e)}"
