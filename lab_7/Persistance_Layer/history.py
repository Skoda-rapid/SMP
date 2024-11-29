import json
import os

class HistoryManager:
    HISTORY_FILE = 'history.json'

    def __init__(self):
        if not os.path.exists(self.HISTORY_FILE):
            with open(self.HISTORY_FILE, 'w') as file:
                json.dump([], file)

    def record(self, action):
        with open(self.HISTORY_FILE, 'r+') as file:
            history = json.load(file)
            history.append(action)
            file.seek(0)
            json.dump(history, file)

    def show_history(self):
        with open(self.HISTORY_FILE, 'r') as file:
            history = json.load(file)
            print("History of actions:")
            for entry in history:
                print(entry)
