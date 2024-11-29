# src/data_saver.py
import json
import csv


class DataSaver:
    def save_as_json(self, data, filename="output.json"):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def save_as_csv(self, data, filename="data.csv"):
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            keys = data[0].keys()
            with open(filename, "w", newline="") as file:
                dict_writer = csv.DictWriter(file, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)
        else:
            raise ValueError("Data should be a list of dictionaries.")
