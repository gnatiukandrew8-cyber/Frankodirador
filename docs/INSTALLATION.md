# Installation & Setup Guide

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gnatiukandrew8-cyber/Frankodirador.git
cd Frankodirador
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install base dependencies
pip install -r requirements.txt

# Install with development dependencies
pip install -e ".[dev]"

# Install with documentation dependencies
pip install -e ".[docs]"
```

## Running Tests

### Run All Tests
```bash
pytest tests/
```

### Run Tests with Coverage
```bash
pytest tests/ --cov=src --cov-report=html
# View coverage report in htmlcov/index.html
```

### Run Specific Test File
```bash
pytest tests/test_main.py
```

### Run Tests with Verbose Output
```bash
pytest tests/ -v
```

### Run Tests with Specific Markers
```bash
pytest tests/ -m unit
pytest tests/ -m integration
```

## Code Quality Tools

### Format Code with Black
```bash
black src/ tests/
```

### Lint Code with Flake8
```bash
flake8 src/ tests/
```

### Type Checking with MyPy
```bash
mypy src/
```

### Sort Imports with isort
```bash
isort src/ tests/
```

### Run All Quality Checks
```bash
black src/ tests/
isort src/ tests/
flake8 src/ tests/
mypy src/
pytest tests/ --cov=src
```

## Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b develop
   git checkout -b feature/your-feature-name
   ```

2. **Make changes**
   - Edit code in `src/`
   - Add corresponding tests in `tests/`

3. **Run tests**
   ```bash
   pytest tests/
   ```

4. **Format and lint**
   ```bash
   black src/ tests/
   flake8 src/ tests/
   ```

5. **Commit changes**
   ```bash
   git add .
   git commit -m "Add description of changes"
   ```

6. **Push to GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**
   - Go to GitHub repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in title and description
   - Submit

## Building Package

### Build Distribution
```bash
python -m pip install build
python -m build
```

This creates:
- `dist/frankodirador-0.1.0-py3-none-any.whl` (wheel)
- `dist/frankodirador-0.1.0.tar.gz` (source distribution)

### Install from Wheel
```bash
pip install dist/frankodirador-0.1.0-py3-none-any.whl
```

## Documentation

### Build Sphinx Documentation
```bash
cd docs/
pip install sphinx sphinx-rtd-theme
make html
```

View in `docs/_build/html/index.html`

## Troubleshooting

### Virtual Environment Issues
```bash
# Deactivate current environment
deactivate

# Remove and recreate
rm -rf venv
python -m venv venv
source venv/bin/activate
```

### Dependency Conflicts
```bash
# Update pip
pip install --upgrade pip

# Clear pip cache
pip cache purge

# Reinstall dependencies
pip install -r requirements.txt
```

### Import Errors
```bash
# Ensure you're in the project root directory
cd /path/to/Frankodirador

# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall package in development mode
pip install -e .
```

## Using the Application

### Import in Your Code
```python
from src.main import Application, hello_world
from src.utils import add, multiply
from src.models import User, Task, Project
from src.config import ConfigManager
from src.logger import get_logger

# Create application
app = Application("MyApp")
app.start()

# Use utilities
result = add(5, 3)  # Returns 8

# Use models
user = User(id=1, username="john", email="john@example.com")

# Use configuration
config_manager = ConfigManager()
config = config_manager.get_config()

# Use logger
logger = get_logger()
logger.info("Application started")
```

### Run as Command Line
```bash
python -m src.main
```

## Environment Variables

Create `.env` file in project root:
```
APP_NAME=Frankodirador
DEBUG=False
LOG_LEVEL=INFO
```

Load in your code:
```python
from dotenv import load_dotenv
import os

load_dotenv()
app_name = os.getenv("APP_NAME")
debug = os.getenv("DEBUG") == "True"
log_level = os.getenv("LOG_LEVEL", "INFO")
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Code style
- Commit messages
- Pull request process
- Issue reporting

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check [CONTRIBUTING.md](CONTRIBUTING.md)
2. Review existing issues on GitHub
3. Create a new issue with detailed description
4. Check [ARCHITECTURE.md](ARCHITECTURE.md) for technical details
