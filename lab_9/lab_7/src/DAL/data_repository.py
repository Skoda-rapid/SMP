# src/data_repository.py
class DataRepository:
    def __init__(self, api_provider):
        self.api_provider = api_provider

    def get_all_data(self, endpoint):
        return self.api_provider.fetch_data(endpoint)
