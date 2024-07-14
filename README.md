# CICD-Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running the Script](#running-the-script)
- [Scheduled Execution with Cron](#scheduled-execution-with-cron)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Description
This project is a Python script designed to fetch and count commits from a specified GitHub repository. It generates an HTML report detailing each commit's ID and message. The script utilizes the GitHub API to retrieve commit data, processes it to extract relevant information, and formats it into an HTML file. This report serves as a convenient summary of repository activity, useful for project management and tracking development progress over time. Users can run the script manually to generate the HTML report. Additionally, the script can be scheduled to run periodically using cron, automating the process of updating and maintaining commit records.

This project is suitable for developers and project managers who need a straightforward tool for tracking commit history and analyzing repository activity visually.

## Features
Fetches commit data using the GitHub API.
Counts and displays commits with their unique identifiers and associated messages.
Generates an HTML report that can be easily viewed or integrated into other web applications.
Supports customization through configuration of the GitHub repository details.

## Installation
### Prerequisites
- Python 3.8+
- Git
- Nginx (for serving HTML)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Ensure Nginx is installed:
    ```bash
    sudo apt update
    sudo apt install -y nginx
    ```

## Usage
### Running the Script Manually
1. Run the script:
    ```bash
    ./run_script.sh
    ```

2. Verify the HTML output at `http://localhost/commits.html`.

### Configuration
- `CD.py`: Modify the script to set your GitHub repository details.

    ```python
    owner = "your-github-username"  # Replace with your GitHub username
    repo = "your-repo-name"  # Replace with your repository name
    ```

## Running the Script
- Ensure the script is executable:
    ```bash
    chmod +x run_script.sh
    ```

- Run the script:
    ```bash
    ./run_script.sh
    ```

## Scheduled Execution with Cron
1. Edit your crontab:
    ```bash
    crontab -e
    ```

2. Add the following line to schedule the script to run at the 1st minute of every hour:
    ```bash
    1 * * * * /path/to/your/run_script.sh >> /path/to/your/logfile.log 2>&1
    ```

3. Save and exit the crontab editor.

## Verifying Cron Job
To check if the cron job is running, inspect the logs:
```bash
grep CRON /var/log/syslog
