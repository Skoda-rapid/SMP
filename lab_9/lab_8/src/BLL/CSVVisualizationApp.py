import os
import pandas as pd
from .factories.VisualizationFactory import VisualizationFactory

file_path = r"d:\SMP\lab_8\data\people.csv"

print(f"Trying to load file from: {file_path}")

class CSVVisualization:
    def __init__(self):
        self.visualization_factory = VisualizationFactory()

    def load_data(self, file_path):
        try:
            if not os.path.isfile(file_path):
                print(f"Файл {file_path} не знайдено.")
                return None
            data = pd.read_csv(file_path)
            print("Дані успішно завантажено.")
            return data
        except Exception as e:
            print(f"Помилка при завантаженні CSV: {e}")
            return None

    def visualize_data(self, data, visualization_type, x="Index", y="Salary"):
        try:
            strategy = self.visualization_factory.create_strategy(visualization_type)

            if x == "Index":
                data_x = pd.Series(data.index)
            else:
                if x not in data.columns:
                    print(f"Колонка {x} не знайдена в даних.")
                    return
                data_x = pd.to_numeric(data[x], errors="coerce")

            if y not in data.columns:
                print(f"Колонка {y} не знайдена в даних.")
                return
            data_y = pd.to_numeric(data[y], errors="coerce")

            if data_x.isnull().any() or data_y.isnull().any():
                print("Одне з значень у колонках має недопустимі або пропущені значення.")
                return

            strategy.visualize(data_x, data_y)

        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Помилка: {e}")

visualization = CSVVisualization()
data = visualization.load_data(file_path)
if data is not None:
    visualization.visualize_data(data, "line", x="Index", y="Salary")
