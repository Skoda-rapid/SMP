# src/api_repository.py
import requests


class APIRepository:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
