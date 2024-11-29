from Repository_Layer.repository import Repository

class DataService:
    def __init__(self, repository):
        self.repository = repository

    def list_posts(self):
        posts = self.repository.get_posts()
        if posts:
            for post in posts:
                print(f"ID: {post['id']}, Title: {post['title']}")
        else:
            print("No posts available.")

    def list_users(self):
        users = self.repository.get_users()
        if users:
            for user in users:
                print(f"ID: {user['id']}, Name: {user['name']}")
        else:
            print("No users available.")
