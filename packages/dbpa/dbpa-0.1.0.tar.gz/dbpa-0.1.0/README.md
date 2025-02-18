# DBPA (Database Personal Assistant)

A natural language interface for database management, powered by AI.

## Features

- 🗣️ Natural Language Queries: Interact with your database using plain English
- 📊 Table Management: Easy interface for managing database tables
- 🎓 Query Training: Learn from and improve query generation
- 📝 Error Analysis: Comprehensive error tracking and analysis
- 🔄 Vector Store: Efficient storage and retrieval of example queries
- 🌐 Multi-Model Support: Works with OpenAI and Groq

## Installation

```bash
pip install dbpa
```

## Quick Start

1. Set up your environment variables:
```bash
export OPENAI_API_KEY="your-api-key"
export POSTGRES_HOST="your-host"
export POSTGRES_DATABASE="your-db"
export POSTGRES_USER="your-user"
export POSTGRES_PASSWORD="your-password"
```

2. Start the DBPA interface:
```bash
dbpa start
```

## Usage

### Basic Query
```python
from dbpa import DatabaseAssistant

assistant = DatabaseAssistant()
result = assistant.query("Show me all customers who made purchases last month")
print(result)
```

### Table Management
```python
from dbpa import TableManager

manager = TableManager()
tables = manager.get_available_tables()
manager.select_tables(["customers", "orders"])
```

### Query Training
```python
from dbpa import QueryTrainer

trainer = QueryTrainer()
trainer.train("Find total sales by product category")
```

## Configuration

DBPA can be configured using a `config.json` file:

```json
{
    "ai_model": "gpt-4",
    "language": "en",
    "max_tokens": 1000,
    "temperature": 0.7
}
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI](https://openai.com/) and [Groq](https://groq.com/)
- Uses [LangChain](https://python.langchain.com/) for LLM interactions
