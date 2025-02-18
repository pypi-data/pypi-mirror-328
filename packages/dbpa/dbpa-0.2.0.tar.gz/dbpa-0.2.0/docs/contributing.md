# Contributing Guide

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/dbpa.git
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```
4. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

### Code Style

We use several tools to maintain code quality:

1. **Black** for code formatting:
   ```bash
   black src/dbpa tests
   ```

2. **isort** for import sorting:
   ```bash
   isort src/dbpa tests
   ```

3. **Ruff** for linting:
   ```bash
   ruff check src/dbpa tests
   ```

4. **mypy** for type checking:
   ```bash
   mypy src/dbpa tests
   ```

### Running Tests

1. **Unit Tests** with pytest:
   ```bash
   pytest tests/unit
   ```

2. **Integration Tests** with Robot Framework:
   ```bash
   robot tests/robot/tests
   ```

3. **Coverage Report**:
   ```bash
   pytest --cov=dbpa --cov-report=html
   ```

## Pull Request Process

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

3. Run all tests and checks:
   ```bash
   # Format code
   black src/dbpa tests
   isort src/dbpa tests
   
   # Run linters
   ruff check src/dbpa tests
   mypy src/dbpa tests
   
   # Run tests
   pytest tests
   robot tests/robot/tests
   ```

4. Push changes and create PR:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request on GitHub

## Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Maintenance tasks

Example:
```
feat(schema): add index optimization suggestions

Add new functionality to SchemaAnalyzer that suggests index optimizations
based on query patterns and table statistics.

Closes #123
```

## Documentation

### API Documentation

When adding new features:

1. Add docstrings to all public functions and classes
2. Follow Google style format
3. Include type hints
4. Document parameters and return values
5. Provide usage examples

Example:
```python
def analyze_indexes(
    self,
    table_name: str,
    schema_info: Dict[str, Any]
) -> List[IndexSuggestion]:
    """Analyze indexes for a table and suggest optimizations.
    
    Args:
        table_name: Name of the table to analyze
        schema_info: Schema information dictionary
        
    Returns:
        List of IndexSuggestion objects with optimization recommendations
        
    Example:
        >>> analyzer = SchemaAnalyzer()
        >>> suggestions = analyzer.analyze_indexes("users", schema_info)
        >>> for suggestion in suggestions:
        ...     print(suggestion.description)
    """
```

### User Documentation

When adding features that affect users:

1. Update relevant sections in `/docs`
2. Add usage examples
3. Document configuration options
4. Include troubleshooting tips

## Testing Guidelines

### Unit Tests

1. Test each function independently
2. Use meaningful test names
3. Follow Arrange-Act-Assert pattern
4. Mock external dependencies
5. Test edge cases and errors

Example:
```python
def test_should_suggest_index_for_frequently_queried_column():
    # Arrange
    analyzer = SchemaAnalyzer()
    schema_info = {
        "tables": {
            "users": {
                "columns": [
                    {"name": "email", "type": "varchar"}
                ]
            }
        }
    }
    
    # Act
    suggestions = analyzer.analyze_indexes("users", schema_info)
    
    # Assert
    assert len(suggestions) == 1
    assert suggestions[0].column == "email"
    assert suggestions[0].reason == "frequently_queried"
```

### Robot Framework Tests

1. Use keyword-driven approach
2. Test end-to-end workflows
3. Include setup and teardown
4. Document test cases

Example:
```robotframework
*** Test Cases ***
Test Should Analyze Database Schema
    [Documentation]    Test schema analysis functionality
    [Tags]    schema    smoke
    
    # Setup
    Connect To Database    ${DB_URL}
    
    # Test
    ${schema_info}=    Analyze Schema
    Should Have Table    users
    Should Have Column    users    email
    
    # Teardown
    Disconnect From Database
```

## Release Process

1. Update version in pyproject.toml
2. Update CHANGELOG.md
3. Create release branch
4. Run all tests and checks
5. Build and test package
6. Create GitHub release
7. Upload to PyPI

## Questions?

- Open an issue on GitHub
- Join our Discord community
- Check existing documentation
- Contact the maintainers
