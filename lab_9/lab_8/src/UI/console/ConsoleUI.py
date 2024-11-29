import os
import sys
import matplotlib as plt
import pandas as pd

lab8_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")
)
sys.path.append(lab8_root)


from lab_8.src.BLL.CSVVisualizationApp import CSVVisualization
from ...BLL.factories import VisualizationFactory
from ...UI.console.ConsoleUIReader import ConsoleUIReader
from ...UI.console.ConsoleUIWriter import ConsoleUIWriter
from shared.constants.global_variables import csv_menu, criteria_menu

file_path = r"d:\SMP\lab_8\data\people.csv"
data = pd.read_csv(file_path)


class ConsoleUI:
    def __init__(self):
        self.console_writer = ConsoleUIWriter()
        self.console_reader = ConsoleUIReader()
        self.csv_visualization = CSVVisualization()

    def load_data(self, file_path):
        try:
            self.console_writer.console_write(f"Завантаження файлу: {file_path}")
            data = pd.read_csv(file_path)
            self.console_writer.console_write("Дані успішно завантажено.")
            return data
        except FileNotFoundError:
            self.console_writer.console_write(f"Файл {file_path} не знайдено.")
        except Exception as e:
            self.console_writer.console_write(
                f"Помилка під час завантаження даних: {e}"
            )
        return None

    def display_menu(self):
        self.console_writer.console_write(csv_menu)
        choice = self.console_reader.console_read()

        match choice:
            case "1":
                self.run_facade()
            case "2":
                self.console_writer.console_write("Вихід з програми.")
            case _:
                self.console_writer.console_write(
                    "Неправильний вибір, спробуйте ще раз."
                )
                self.display_menu()

    def run_facade(self):
        self.console_writer.console_write(criteria_menu)
        choice = self.console_reader.console_read()

        match choice:
            case "1":
                data = self.load_data(file_path)
                if data is not None:
                    self.display_extreme_values(data)
            case "2":
                data = self.load_data(file_path)
                if data is not None:
                    self.filter_data(data)
            case "3":
                data = self.load_data(file_path)
                if data is not None:
                    graph_type = self.console_reader.console_read(
                        "Введіть тип графіка (line / bar): "
                    )

                    self.console_writer.console_write(
                        f"Доступні колонки: {list(data.columns)}"
                    )
                    x_column = self.console_reader.console_read(
                        "Введіть назву колонки для X-осі: "
                    )
                    y_column = self.console_reader.console_read(
                        "Введіть назву колонки для Y-осі: "
                    )

                    if x_column in data.columns and y_column in data.columns:
                        self.run_visualization(graph_type, data, x_column, y_column)
                    else:
                        self.console_writer.console_write(
                            "Помилка: Обрані колонки не знайдені в даних."
                        )
            case "4":
                data = self.load_data(file_path)
                if data is not None:
                    self.add_graph(data)
            case "5":
                data = self.load_data(file_path)
                if data is not None:
                    self.export_as_png(data)
            case "6":
                self.console_writer.console_write("Вихід з програми.")
            case _:
                self.console_writer.console_write(
                    "Неправильний вибір, спробуйте ще раз."
                )
                self.run_facade()

    def display_extreme_values(self, data):
        if data is None:
            self.console_writer.console_write(
                "Неможливо відобразити екстремальні значення: дані не завантажені."
            )
            return
        try:
            min_values = data.min()
            max_values = data.max()

            self.console_writer.console_write("Мінімальні значення по стовпцях:")
            for col, value in min_values.items():
                self.console_writer.console_write(f"{col}: {value}")

            self.console_writer.console_write("\nМаксимальні значення по стовпцях:")
            for col, value in max_values.items():
                self.console_writer.console_write(f"{col}: {value}")
        except Exception as e:
            self.console_writer.console_write(
                f"Помилка під час обробки екстремальних значень: {e}"
            )

    def filter_data(self, data):
        try:
            self.console_writer.console_write("Введіть назву стовпця для фільтрації:")
            column = self.console_reader.console_read()

            self.console_writer.console_write("Введіть значення для фільтрації:")
            if data[column].dtype == "object":
                value = self.console_reader.console_read()
            else:
                value = float(self.console_reader.console_read())

            filtered_data = data[data[column] == value]

            if not filtered_data.empty:
                self.console_writer.console_write("Відфільтровані дані:")
                self.console_writer.console_write(filtered_data.to_string(index=False))
            else:
                self.console_writer.console_write(
                    "Жодних даних не знайдено за критерієм фільтрації."
                )
        except KeyError:
            self.console_writer.console_write(
                f"Стовпець '{column}' не знайдено в даних."
            )
        except ValueError:
            self.console_writer.console_write("Некоректне значення для фільтрації.")
        except Exception as e:
            self.console_writer.console_write(f"Помилка під час фільтрації даних: {e}")

    def choose_and_visualize(self):
        graph_type = self.console_reader.console_read(
            "Введіть тип графіка (line/bar): "
        )
        self.csv_visualization.process_csv(data, graph_type)

    def add_graph(self, data):
        try:
            self.console_writer.console_write(
                "Виберіть тип графіка (1 - Лінійний, 2 - Стовпчастий):"
            )
            choice = self.console_reader.console_read()

            strategy = VisualizationFactory.get_visualization_strategy(choice)

            data_x = data["x"]
            data_y = data["y"]

            strategy.visualize(data_x, data_y)

            self.console_writer.console_write("Графік успішно додано.")
        except Exception as e:
            self.console_writer.console_write(f"Помилка під час додавання графіка: {e}")

    def export_as_png(self, data):
        try:
            self.console_writer.console_write(
                "Виберіть тип графіка для експорту (1 - Лінійний, 2 - Стовпчастий):"
            )
            choice = self.console_reader.console_read()

            strategy = VisualizationFactory.get_visualization_strategy(choice)

            data_x = data["x"]
            data_y = data["y"]

            strategy.visualize(data_x, data_y)

            filename = "exported_graph.png"
            plt.savefig(filename)
            plt.close()

            self.console_writer.console_write(
                f"Графік успішно експортовано як {filename}."
            )
        except Exception as e:
            self.console_writer.console_write(f"Помилка під час експорту графіка: {e}")

    def run_visualization(self, graph_type, data, x_column, y_column):
        if data is not None:
            self.csv_visualization.visualize_data(data, graph_type, x_column, y_column)
