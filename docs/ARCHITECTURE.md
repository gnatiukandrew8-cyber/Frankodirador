# Architecture Guide

## Project Structure

```
Frankodirador/
├── src/                    # Source code
│   ├── __init__.py        # Package initialization
│   ├── main.py            # Core application class
│   ├── utils.py           # Utility functions
│   ├── config.py          # Configuration management
│   ├── logger.py          # Logging functionality
│   └── models.py          # Data models
├── tests/                 # Test suite
│   ├── conftest.py        # Pytest configuration and fixtures
│   ├── test_main.py       # Tests for main module
│   ├── test_utils.py      # Tests for utilities
│   ├── test_config.py     # Tests for configuration
│   ├── test_logger.py     # Tests for logging
│   └── test_models.py     # Tests for data models
├── docs/                  # Documentation
│   ├── CONTRIBUTING.md    # Contribution guidelines
│   ├── CHANGELOG.md       # Version history
│   ├── ARCHITECTURE.md    # This file
│   ├── INSTALLATION.md    # Setup guide
│   └── API_REFERENCE.md   # API documentation
├── .github/workflows/     # CI/CD workflows
│   └── ci.yml            # Continuous integration
├── .gitignore            # Git exclusions
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup
└── README.md            # Project overview
```

## Module Organization

### `src/` Directory

#### `main.py`
Core application logic with the `Application` class that manages application lifecycle (start/stop/status).

- **Application**: Main application class with lifecycle management
- **hello_world()**: Simple greeting function

#### `utils.py`
Arithmetic and general utility functions.

- **add()**: Addition function
- **subtract()**: Subtraction function
- **multiply()**: Multiplication function
- **divide()**: Division function with error handling

#### `config.py`
Configuration management using the Singleton pattern.

- **Config**: Data class for application configuration
- **ConfigManager**: Singleton manager for global configuration access

#### `logger.py`
Logging functionality using the Singleton pattern.

- **Logger**: Custom logger with multiple log levels
- **get_logger()**: Helper function to get logger instance

#### `models.py`
Data models for users, tasks, and projects.

- **User**: User data model with profile information
- **Task**: Task data model with status and completion tracking
- **Project**: Project data model with member and task management

### `tests/` Directory

Comprehensive test suite using pytest.

- **test_main.py**: Tests for application lifecycle and greeting function
- **test_utils.py**: Tests for arithmetic functions
- **test_config.py**: Tests for configuration management
- **test_logger.py**: Tests for logging functionality
- **test_models.py**: Tests for data models
- **conftest.py**: Pytest fixtures and configuration

## Design Patterns

### Singleton Pattern
Used in `ConfigManager` and `Logger` to ensure only one instance exists throughout the application lifecycle.

```python
class ConfigManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Data Classes
Models use `@dataclass` decorator for clean, immutable-like data structures.

```python
@dataclass
class User:
    id: int
    username: str
    email: str
```

## Testing Strategy

### Test Organization
- Unit tests for individual functions and classes
- Integration tests for component interactions
- Test fixtures for common test data

### Test Markers
```
@pytest.mark.unit       # Unit tests
@pytest.mark.integration # Integration tests
@pytest.mark.slow       # Slow running tests
```

### Coverage
Target: >80% code coverage
Run: `pytest tests/ --cov=src --cov-report=html`

## CI/CD Pipeline

### GitHub Actions Workflow
- Triggers on push to `main` and `develop` branches
- Tests on Python 3.9, 3.10, 3.11
- Runs pytest with coverage reporting
- Uploads coverage to Codecov

## Dependencies

### Core Dependencies
- No external runtime dependencies (lightweight)

### Development Dependencies
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Linting
- **mypy**: Type checking
- **isort**: Import sorting

### Documentation Dependencies
- **sphinx**: Documentation generation
- **sphinx-rtd-theme**: ReadTheDocs theme

## Development Workflow

1. Create feature branch from `develop`
2. Write code and tests
3. Run tests locally: `pytest tests/`
4. Format code: `black src/ tests/`
5. Lint code: `flake8 src/ tests/`
6. Type check: `mypy src/`
7. Push to GitHub and create PR
8. CI/CD runs automated checks
9. Merge to `develop` after approval
10. Merge to `main` for releases

## Future Enhancements

- Database integration (SQLAlchemy)
- REST API (FastAPI/Flask)
- Authentication & Authorization
- Caching layer (Redis)
- Message queue (Celery)
- Monitoring & Observability
- Docker containerization
- Kubernetes deployment
