# SIEM System

## Description
This project is a Security Information and Event Management (SIEM) system that collects and analyzes security data from various sources to detect and respond to threats.

## Skills
- Python
- Log Analysis
- Networking
- Real-Time Monitoring
- Email/SMS Notifications

## Features
- Log collection from multiple sources
- Real-time log monitoring
- Advanced log analysis with pattern matching and anomaly detection
- Email/SMS alert notifications

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Barrosleo/SIEM-System.git
    ```
2. Navigate to the project directory:
    ```bash
    cd SIEM-System/src
    ```
3. Install required libraries:
    ```bash
    pip install watchdog smtplib
    ```
4. Run the main script:
    ```bash
    python main.py
    ```

## Usage
- Place your log files in the `logs/` directory.
- Run the main script to analyze the logs and generate alerts.
