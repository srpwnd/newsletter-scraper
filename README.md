# Newsletter Scraper Project

This project is a web scraper designed to extract newsletter data from the [Bizztreat newsletter site](https://www.bizztreat.com/newsletter-blog) using Scrapy and `dlt`. The data can be stored in both CSV and Parquet formats.

## Features
- Scrapes newsletters (title, date, author, URL, image URL) from the Bizztreat website.
- Supports multiple output formats: CSV and Parquet.
- Utilizes `dlt` for data pipeline management and local file storage.
- Includes a Makefile for easier management of tasks such as running the scraper, installing dependencies, running tests, linting, and formatting.
- Dockerized for easy deployment and isolated execution.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Makefile Commands](#makefile-commands)
4. [Testing](#testing)
5. [Docker Setup](#docker-setup)

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/srpwnd/newsletter-scraper.git
    cd newsletter-scraper
    ```

2. **Set up a Python virtual environment:**
    The project uses a `venv` (virtual environment) to manage dependencies.

    Run the following command to create and activate the virtual environment:
    ```bash
    make venv
    ```

3. **Install the dependencies:**
    Once the virtual environment is active, install all the necessary dependencies by running:
    ```bash
    make install
    ```

---

## Usage

To run the scraper, use the following command:

```bash
make run
```

This will execute the main scraper pipeline defined in `scraping_pipeline.py`.

You can also clean up data files and virtual environments using:

```bash
make clean
```

---

## Makefile Commands

The Makefile provides a series of predefined commands to help with project management. Here is a list of the most common commands:

| Command        | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| `make run`     | Runs the scraping script (`scraping_pipeline.py`) within the virtual environment. |
| `make venv`    | Creates a Python virtual environment using `venv` and installs dependencies. |
| `make install` | Installs dependencies from the `requirements.txt` file into the virtual environment. |
| `make freeze`  | Freezes the current set of installed dependencies into `requirements.txt`.  |
| `make test`    | Runs the unit and integration tests using `unittest`.                       |
| `make lint`    | Lints the codebase using `ruff` to enforce coding standards and automatically fixes issues. |
| `make format`  | Formats the codebase using `ruff` formatting rules.                         |
| `make clean`   | Cleans up generated files such as `__pycache__`, virtual environments, CSV/Parquet data files. |
| `make clean-data` | Cleans only the data files (CSV, Parquet) stored in `_storage` directories. |
| `make clean-venv` | Removes the virtual environment folder.                                   |

---

## Testing

Unit and integration tests are located in the `tests/` directory. To run all tests, use:

```bash
make test
```

This will automatically discover and run all the test cases using `unittest`.

---

## Docker Setup

The project is Dockerized to simplify running in isolated environments. You can use Docker and Docker Compose to run the scraper without needing to install the dependencies manually.

### Docker

1. **Build the Docker image:**
    ```bash
    docker build -t newsletter-scraper .
    ```

2. **Run the scraper using Docker:**
    ```bash
    docker run newsletter-scraper
    ```

### Docker Compose

1. **Run the scraper with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

This will build the image (if necessary) and run the scraper automatically inside a container.

---

## Storage Location

The output data is stored in the `_storage` directory, which contains subdirectories for both CSV and Parquet formats, depending on the pipeline you use.
