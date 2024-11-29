from API_Layer.api_client import APIClient
from Repository_Layer.repository import Repository
from Service_Layer.service import DataService
from Persistance_Layer.history import HistoryManager

class Factory:
    @staticmethod
    def create_api_client():
        return APIClient()

    @staticmethod
    def create_repository(api_client):
        return Repository(api_client)

    @staticmethod
    def create_data_service(repository):
        return DataService(repository)

    @staticmethod
    def create_history_manager():
        return HistoryManager()
