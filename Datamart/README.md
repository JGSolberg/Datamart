# DQ Datamart

**Datamart** is a Python application designed to interact with the Collibra REST API, process and store data, and integrate logging functionality. This application fetches asset and user data from Collibra, processes it, and stores it in a database. For testing, it uses SQLite and mock data.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Directory Structure](#directory-structure)
- [License](#license)

## Features
- Fetches data from the Collibra REST API.
- Processes and converts data, including date and time conversion.
- Logs information to the console and/or a log file.
- Stores data in an SQLite database for testing.
- Supports integration with Google Cloud databases for production.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/datamart.git
    cd datamart
    ```

2. **Set Up a Virtual Environment**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` File**

    Copy `.env.example` to `.env` and set your environment variables.

    ```bash
    cp .env.example .env
    ```

    Update the `.env` file with your configuration.

## Usage

### Running the Application

To run the application, execute:

```bash
python main.py --log_name <job_id> --write_logs
```

Replace `<job_id>` with a UUID for log file naming. Use `--write_logs` to enable file logging. Omit it to log only to the console.

### Configuration

- **Logging**: Configure logging in `logger/logging_config.py` and `logger/logging_config.ini`.
- **Database**: Set `DATABASE` in `db_handler/db_sqlite.py` for SQLite or update for Google Cloud databases in production.
- **API Data**: Define API endpoints and mock data in `Collibra/api.py`.

## Testing

To run tests, use:

```bash
python -m unittest discover -s tests
```

This will discover and run all test cases defined in the `tests` directory.

### Available Tests

- **`tests/test_logger.py`**: Tests logging functionality.
- **`tests/test_api.py`**: Tests API data fetching and processing.
- **`tests/test_db_handler.py`**: Tests database operations.
- **`tests/test_main.py`**: Tests the `main.py` script.

## Directory Structure

```
Datamart/
    main.py               # Main script to run the application
    _logs/                # Directory for log files
    logger/
        __init__.py       # Initialization for logger package
        logging_config.py # Configures logging
        logging_config.ini # Logging configuration file
    Collibra/
        __init__.py       # Initialization for Collibra package
        api.py            # Handles API calls and mock data
    db_handler/
        __init__.py       # Initialization for db_handler package
        db_sqlite.py      # SQLite database handler
    tests/
        __init__.py       # Initialization for tests package
        test_logger.py    # Tests for logging
        test_api.py       # Tests for API functions
        test_db_handler.py # Tests for database handler
        test_main.py      # Tests for main script
    .env                  # Environment variables
    requirements.txt      # Python dependencies
    README.md             # This file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify the README as needed based on your project's specific details and requirements.