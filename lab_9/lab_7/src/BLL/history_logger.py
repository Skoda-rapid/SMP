# src/history_logger.py
import datetime

class HistoryLogger:
    def __init__(self):
        self.history = []

    def log_request(self, request, response):
        timestamp = datetime.datetime.now()
        self.history.append({"timestamp": timestamp, "request": request, "response": response})

    def show_history(self):
        for entry in self.history:
            print(f"{entry['timestamp']}: Request - {entry['request']}, Response - {entry['response']}")
