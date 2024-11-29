from API_Layer.api_client import APIClient

class Repository:
    def __init__(self, api_client):
        self.api_client = api_client
        self.cache = {}

    def get_posts(self):
        if 'posts' not in self.cache:
            self.cache['posts'] = self.api_client.get_data('posts')
        return self.cache['posts']

    def get_users(self):
        if 'users' not in self.cache:
            self.cache['users'] = self.api_client.get_data('users')
        return self.cache['users']
