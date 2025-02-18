# Database Personal Assistant (DBPA)

DBPA is an AI-powered database management system that provides advanced text-to-SQL capabilities through a modular, agent-based architecture.

## Features

- **Natural Language to SQL**: Convert natural language queries into SQL using advanced AI models
- **Schema Analysis**: Intelligent database schema analysis and optimization suggestions
- **Query Templates**: Generate and manage query templates based on database structure
- **Multi-Agent Architecture**: Modular design with specialized agents for different tasks
- **Vector Store**: Efficient storage and retrieval of query examples
- **Multilingual Support**: Process queries in multiple languages
- **Streamlit UI**: User-friendly interface for managing the system

## Installation

```bash
pip install dbpa
```

For development installation:

```bash
pip install dbpa[dev]
```

## Quick Start

```python
from dbpa.txt2sql.agents.schema import SchemaAnalyzer
from dbpa.txt2sql.vector_store import VectorStore

# Initialize components
analyzer = SchemaAnalyzer()
store = VectorStore()

# Analyze database schema
schema_info = analyzer.analyze_schema("postgresql://user:pass@localhost/db")

# Generate query templates
templates = analyzer.generate_templates(schema_info)

# Store templates for future use
store.add_examples(templates)

# Convert natural language to SQL
query = "Find all users who joined last month"
sql = store.find_similar_queries(query)
```

## Architecture

DBPA uses a multi-agent architecture where each agent specializes in a specific task:

- **SchemaAnalysisAgent**: Analyzes database structure and generates optimized templates
- **DataManagementAgent**: Manages vector store data and query examples
- **QualityAssuranceAgent**: Ensures query quality and performance
- **TranslationAgent**: Handles multilingual query processing
- **MonitoringAgent**: Tracks system performance and usage
- **SecurityAgent**: Manages access control and security

## Documentation

For detailed documentation, visit:
- [API Reference](api.md)
- [User Guide](user_guide.md)
- [Contributing Guide](contributing.md)
- [Security](security.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
