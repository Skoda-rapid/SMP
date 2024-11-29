# src/history_manager.py
import json
import os

class HistoryManager:
    def __init__(self, history_file="history.json"):
        self.history_file = history_file

    def save_to_history(self, command, data):
        history = self.load_history()
        history.append({"command": command, "data": data})
        with open(self.history_file, "w") as file:
            json.dump(history, file, indent=4)

    def load_history(self):
        if not os.path.exists(self.history_file):
            return []
        with open(self.history_file, "r") as file:
            return json.load(file)
