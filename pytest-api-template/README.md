# Pytest API Automation Template

This is a professional, industry-standard template for API automation testing using Python and Pytest.

## Features

- **Base Client Abstraction**: Centralized request handling with `requests.Session`.
- **Environment Configuration**: Managed via `python-dotenv` and Pydantic-like settings.
- **Advanced Logging**: Uses `loguru` for structured and beautiful logs.
- **Test Data Generation**: Integrated with `Faker` for dynamic data.
- **Reporting**: Generates HTML reports and Allure results.
- **Professional Structure**: Organized for scalability and maintainability.

## Project Structure

```text
pytest-api-template/
├── api/                # API clients (Base and Resource-specific)
├── config/             # Configuration management
├── data/               # Static test data (JSON, CSV)
├── tests/              # Test cases and conftest.py
├── utils/              # Common utilities and helpers
├── .env.example        # Environment variable template
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Environment**:
   Copy `.env.example` to `.env` and fill in your values.
   ```bash
   cp .env.example .env
   ```

3. **Run Tests**:
   ```bash
   pytest
   ```

4. **Generate Allure Report** (optional):
   ```bash
   allure serve reports/allure-results
   ```

## Best Practices Followed

- **DRY (Don't Repeat Yourself)**: Using fixtures and base classes.
- **Type Hinting**: Improved code clarity and IDE support.
- **Encapsulation**: API logic is separated from test logic.
- **Logging**: Every request and response is logged for easier debugging.
- **Cleanup**: Fixtures handle resource teardown.
