# src/api_provider.py
import requests
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

class ApiProvider:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def fetch_data(self, endpoint):
        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching data from API: {e}")
