import os
import json
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LogHandler(FileSystemEventHandler):
    def __init__(self, log_directories):
        self.log_directories = log_directories

    def on_modified(self, event):
        if event.src_path.endswith(".log"):
            logs = collect_logs(self.log_directories)
            alerts = analyze_logs(logs)
            with open("../docs/alerts.json", 'w') as alert_file:
                json.dump(alerts, alert_file)
            print(f"Analysis complete. {len(alerts)} alerts found.")

def collect_logs(log_directories):
    logs = []
    for log_directory in log_directories:
        for filename in os.listdir(log_directory):
            if filename.endswith(".log"):
                with open(os.path.join(log_directory, filename), 'r') as file:
                    logs.extend(file.readlines())
    return logs

def analyze_logs(logs):
    alerts = []
    for log in logs:
        if "ERROR" in log or "WARNING" in log:
            alerts.append(log)
        if "failed login" in log.lower():
            alerts.append(f"Security Alert: {log}")
    return alerts

def main():
    log_directories = ["../logs/system", "../logs/application", "../logs/network"]
    event_handler = LogHandler(log_directories)
    observer = Observer()
    for log_directory in log_directories:
        observer.schedule(event_handler, log_directory, recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
