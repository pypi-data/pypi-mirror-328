# API Reference

## Schema Analysis

### SchemaAnalyzer

The `SchemaAnalyzer` class provides functionality for analyzing database schemas and generating query templates.

```python
from dbpa.txt2sql.agents.schema import SchemaAnalyzer

analyzer = SchemaAnalyzer(name="SchemaAnalyzer")
```

#### Methods

##### analyze_schema
```python
def analyze_schema(self, connection_string: str) -> Dict[str, Any]
```
Analyzes a database schema and returns detailed information about tables, relationships, and constraints.

**Parameters:**
- `connection_string`: Database connection string (e.g., "postgresql://user:pass@localhost/db")

**Returns:**
- Dictionary containing schema information:
  - tables: Table definitions and column information
  - relationships: Foreign key relationships
  - indexes: Index definitions
  - constraints: Database constraints

##### generate_templates
```python
def generate_templates(
    self,
    schema_info: Dict[str, Any],
    schema_hash: str
) -> List[QueryExample]
```
Generates query templates based on schema information.

**Parameters:**
- `schema_info`: Schema information from analyze_schema
- `schema_hash`: Unique identifier for the schema

**Returns:**
- List of QueryExample objects containing natural language and SQL query pairs

### TemplateGenerator

The `TemplateGenerator` class manages the generation and storage of query templates.

```python
from dbpa.txt2sql.agents.schema import TemplateGenerator

generator = TemplateGenerator(
    name="TemplateGenerator",
    template_path=Path("templates.json")
)
```

#### Methods

##### generate_templates
```python
def generate_templates(
    self,
    schema_info: Dict[str, Any],
    schema_hash: str
) -> List[QueryExample]
```
Generates query templates for a given schema.

**Parameters:**
- `schema_info`: Schema information
- `schema_hash`: Schema identifier

**Returns:**
- List of QueryExample objects

## Vector Store

### VectorStore

The `VectorStore` class provides efficient storage and retrieval of query examples using vector embeddings.

```python
from dbpa.txt2sql.vector_store import VectorStore

store = VectorStore(
    embedding_model="all-MiniLM-L6-v2",
    index_path="vectors.index"
)
```

#### Methods

##### add_examples
```python
def add_examples(self, examples: List[QueryExample]) -> None
```
Adds query examples to the vector store.

**Parameters:**
- `examples`: List of QueryExample objects

##### find_similar_queries
```python
def find_similar_queries(
    self,
    query: str,
    top_k: int = 5
) -> List[QueryExample]
```
Finds similar queries in the vector store.

**Parameters:**
- `query`: Natural language query
- `top_k`: Number of results to return

**Returns:**
- List of similar QueryExample objects

## Models

### QueryExample

The `QueryExample` class represents a natural language to SQL query pair.

```python
from dbpa.txt2sql.models.examples import QueryExample

example = QueryExample(
    natural_query="Find all active users",
    sql_query="SELECT * FROM users WHERE status = 'active'",
    language="en",
    database_type="postgresql",
    schema_hash="abc123",
    metadata={"template_type": "select_where"}
)
```

#### Attributes

- `natural_query`: Natural language query
- `sql_query`: Corresponding SQL query
- `language`: Query language (e.g., "en")
- `database_type`: Type of database (e.g., "postgresql")
- `schema_hash`: Schema identifier
- `metadata`: Additional metadata about the query

### Template

The `Template` class represents a query template.

```python
from dbpa.txt2sql.models.agent_models import Template

template = Template(
    name="select_where",
    natural_template="Find {table} where {column} equals {value}",
    sql_template="SELECT * FROM {table} WHERE {column} = :{value}",
    metadata={"type": "basic"}
)
```

#### Attributes

- `name`: Template identifier
- `natural_template`: Natural language template
- `sql_template`: SQL query template
- `metadata`: Template metadata
