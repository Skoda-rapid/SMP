# src/main.py
import sys
import os

from shared.logger import Logger

sys.path.append(os.path.join(os.path.dirname(__file__), "."))

from DAL.api_provider import ApiProvider
from DAL.data_repository import DataRepository
from BLL.unit_of_work import UnitOfWork
from UI.user_interface import UserInterface
from DAL.data_parser import DataParser
from DAL.data_saver import DataSaver
from BLL.error_handler import ErrorHandler
from BLL.history_logger import HistoryLogger


def main():
    Logger.log("Лабораторна 7 запущена")
    
    api_provider = ApiProvider()
    repository = DataRepository(api_provider)
    unit_of_work = UnitOfWork(repository)
    ui = UserInterface()
    parser = DataParser()
    saver = DataSaver()
    error_handler = ErrorHandler()
    logger = HistoryLogger()

    print("Welcome to the data management app!")

    while True:
        user_input = input("\nEnter command ('get posts', 'get users', 'exit'): ")

        command = parser.parse_command(user_input)
        if command is None:
            print("Invalid command. Please try again.")
            continue

        try:
            if command == "exit":
                print("Exiting the program.")
                break
            elif command == "get posts":
                unit_of_work.load_data("posts")
                data = unit_of_work.commit()
                ui.display_table(data)

                logger.log_request(command, data)
                saver.save_as_json(data)
                saver.save_as_csv(data)
            elif command == "get users":
                unit_of_work.load_data("users")
                data = unit_of_work.commit()
                ui.display_table(data)

                logger.log_request(command, data)
                saver.save_as_json(data)
                saver.save_as_csv(data)
            else:
                print("Unknown command.")

        except Exception as e:
            error_handler.handle_error(e)

