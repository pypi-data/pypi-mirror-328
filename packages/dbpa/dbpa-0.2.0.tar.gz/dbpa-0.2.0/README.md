# Database Personal Assistant (DBPA)

[![PyPI version](https://badge.fury.io/py/dbpa.svg)](https://badge.fury.io/py/dbpa)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

DBPA is an advanced AI-powered database management system that provides natural language interface for database operations. It uses a modular, agent-based architecture to convert natural language queries into optimized SQL, analyze database schemas, and provide intelligent suggestions.

## Features

- **Natural Language to SQL**: Convert human language queries into optimized SQL
- **Schema Analysis**: Intelligent database schema analysis and optimization
- **Query Templates**: Dynamic generation and management of query templates
- **Multi-Agent Architecture**: Specialized agents for different tasks
- **Vector Store**: Efficient semantic search for query examples
- **Multilingual Support**: Process queries in multiple languages
- **Security-First**: Built-in security best practices
- **Modern UI**: Streamlit-based user interface

## Installation

```bash
pip install dbpa
```

For development:

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
schema_info = analyzer.analyze_schema(
    "postgresql://user:pass@localhost/db"
)

# Generate query templates
templates = analyzer.generate_templates(schema_info)

# Store templates
store.add_examples(templates)

# Convert natural language to SQL
query = "Find all active users who registered last month"
results = store.find_similar_queries(query)
sql = results[0].sql_query
```

## Architecture

DBPA uses a multi-agent architecture with specialized components:

### Core Agents
- **SchemaAnalysisAgent**: Database structure analysis
- **DataManagementAgent**: Vector store management
- **QualityAssuranceAgent**: Query optimization
- **TranslationAgent**: Multilingual support
- **MonitoringAgent**: Performance tracking
- **SecurityAgent**: Access control

### Key Components
- **Vector Store**: Semantic search engine
- **Template Generator**: Query pattern management
- **Schema Analyzer**: Database structure analysis
- **UI Components**: Streamlit interface

## Documentation

- [API Reference](docs/api.md)
- [User Guide](docs/user_guide.md)
- [Contributing](docs/contributing.md)
- [Security](docs/security.md)

## Security

DBPA implements several security measures:

- Query sanitization
- Input validation
- Access control
- Secure credential management
- Audit logging

See our [Security Guide](docs/security.md) for details.

## Testing

Run the test suite:

```bash
# Unit tests
pytest tests/unit

# Integration tests
robot tests/robot/tests

# Coverage report
pytest --cov=dbpa
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](docs/contributing.md) for details.

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Run the test suite
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- SQLAlchemy team for the amazing database toolkit
- Sentence Transformers for vector embeddings
- Streamlit for the UI framework
- PyPI for package hosting

## Contact

- GitHub: [achimdehnert/dbpa](https://github.com/achimdehnert/dbpa)
- Issues: [GitHub Issues](https://github.com/achimdehnert/dbpa/issues)

## Roadmap

- [ ] Support for more database types
- [ ] Advanced query optimization
- [ ] Enhanced multilingual capabilities
- [ ] Real-time performance monitoring
- [ ] Extended security features
