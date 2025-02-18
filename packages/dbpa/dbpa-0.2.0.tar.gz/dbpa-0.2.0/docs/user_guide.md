# User Guide

## Installation

### Basic Installation

Install DBPA using pip:

```bash
pip install dbpa
```

### Development Installation

For development, install with additional tools:

```bash
pip install dbpa[dev]
```

## Configuration

### Database Connection

DBPA supports various database types through SQLAlchemy. Here's how to connect:

```python
from dbpa.txt2sql.agents.schema import SchemaAnalyzer

# PostgreSQL
analyzer = SchemaAnalyzer()
schema = analyzer.analyze_schema("postgresql://user:pass@localhost/db")

# MySQL
schema = analyzer.analyze_schema("mysql://user:pass@localhost/db")

# SQLite
schema = analyzer.analyze_schema("sqlite:///path/to/db.sqlite")
```

### Vector Store Setup

Configure the vector store for query matching:

```python
from dbpa.txt2sql.vector_store import VectorStore

store = VectorStore(
    embedding_model="all-MiniLM-L6-v2",  # Default model
    index_path="vectors.index",          # Save embeddings
    dimension=384,                       # Embedding dimension
    distance_metric="cosine"             # Similarity metric
)
```

## Basic Usage

### Schema Analysis

1. Analyze database schema:
```python
schema_info = analyzer.analyze_schema(connection_string)
```

2. Generate query templates:
```python
templates = analyzer.generate_templates(schema_info)
```

3. Store templates:
```python
store.add_examples(templates)
```

### Query Processing

1. Convert natural language to SQL:
```python
query = "Show me all users who registered this month"
similar_queries = store.find_similar_queries(query)
sql = similar_queries[0].sql_query
```

2. Execute query:
```python
from sqlalchemy import create_engine, text

engine = create_engine(connection_string)
with engine.connect() as conn:
    result = conn.execute(text(sql))
    data = result.fetchall()
```

## Advanced Features

### Custom Templates

Create custom query templates:

```python
from dbpa.txt2sql.models.agent_models import Template

template = Template(
    name="user_registration",
    natural_template="Find users who registered between {start_date} and {end_date}",
    sql_template="""
        SELECT * FROM users 
        WHERE registration_date BETWEEN :start_date AND :end_date
    """,
    metadata={"type": "date_range"}
)
```

### Multilingual Support

Process queries in different languages:

```python
# English
query_en = "Find all active users"

# German
query_de = "Finde alle aktiven Benutzer"

# Process queries
results_en = store.find_similar_queries(query_en, language="en")
results_de = store.find_similar_queries(query_de, language="de")
```

### Schema Optimization

Get schema optimization suggestions:

```python
from dbpa.txt2sql.agents.schema import SchemaAnalyzer

analyzer = SchemaAnalyzer()
schema_info = analyzer.analyze_schema(connection_string)

# Get optimization suggestions
suggestions = analyzer.get_optimization_suggestions(schema_info)

for suggestion in suggestions:
    print(f"Type: {suggestion.type}")
    print(f"Description: {suggestion.description}")
    print(f"SQL: {suggestion.sql}")
```

## Best Practices

### Performance Optimization

1. **Index Management**
   - Create indexes for frequently queried columns
   - Monitor index usage
   - Remove unused indexes

2. **Query Templates**
   - Create templates for common query patterns
   - Use parameterized queries
   - Include metadata for better matching

3. **Vector Store**
   - Regularly update embeddings
   - Remove outdated examples
   - Monitor similarity scores

### Security

1. **Connection Safety**
   - Use environment variables for credentials
   - Implement connection pooling
   - Set appropriate timeouts

2. **Query Validation**
   - Validate user input
   - Use parameterized queries
   - Implement query timeout limits

3. **Access Control**
   - Implement user authentication
   - Set up role-based access
   - Monitor query patterns

## Troubleshooting

### Common Issues

1. **Connection Problems**
   ```python
   # Test connection
   from sqlalchemy import create_engine
   
   try:
       engine = create_engine(connection_string)
       with engine.connect() as conn:
           pass
   except Exception as e:
       print(f"Connection failed: {str(e)}")
   ```

2. **Query Matching Issues**
   ```python
   # Debug similarity scores
   results = store.find_similar_queries(
       query,
       include_scores=True,
       top_k=5
   )
   for result in results:
       print(f"Score: {result.score}")
       print(f"Query: {result.natural_query}")
   ```

3. **Schema Analysis Errors**
   ```python
   # Enable detailed logging
   import logging
   logging.basicConfig(level=logging.DEBUG)
   
   schema_info = analyzer.analyze_schema(
       connection_string,
       verbose=True
   )
   ```

### Getting Help

- Check the [GitHub Issues](https://github.com/achimdehnert/dbpa/issues)
- Join our [Discord Community](https://discord.gg/dbpa)
- Read the [FAQ](faq.md)
- Contact support at support@dbpa.io
