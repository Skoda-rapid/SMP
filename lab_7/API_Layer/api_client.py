import requests

class APIClient:
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    def get_data(self, endpoint):
        try:
            response = requests.get(f'{self.BASE_URL}/{endpoint}')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return None
