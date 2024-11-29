from API_Layer.api_client import APIClient
from Repository_Layer.repository import Repository
from Service_Layer.service import DataService
from Persistance_Layer.history import HistoryManager 
from Factory_Layer.factory import Factory
from Service_Layer.unit_of_work import UnitOfWork
from input_parser import InputParser

def main():
    # Створюємо об'єкти через фабрику
    api_client = Factory.create_api_client()
    repository = Factory.create_repository(api_client)
    service = Factory.create_data_service(repository)
    history_manager = Factory.create_history_manager()
    unit_of_work = UnitOfWork(history_manager)

    while True:
        print("\nChoose an option:")
        print("1. List posts")
        print("2. List users")
        print("3. View history")
        print("4. Parse input")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            service.list_posts()
            unit_of_work.record_action("Listed posts")
        elif choice == '2':
            service.list_users()
            unit_of_work.record_action("Listed users")
        elif choice == '3':
            history_manager.show_history()
        elif choice == '4':
            user_input = input("Enter text to parse: ")
            parsed_result = InputParser.parse_input(user_input)
            print("Parsed data:", parsed_result)
            unit_of_work.record_action(f"Parsed input: {parsed_result}")
        elif choice == '5':
            unit_of_work.commit()
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
