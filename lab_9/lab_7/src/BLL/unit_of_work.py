
# src/unit_of_work.py
class UnitOfWork:
    def __init__(self, repository):
        self.repository = repository
        self.data = None

    def load_data(self, endpoint):
        self.data = self.repository.get_all_data(endpoint)

    def commit(self):
        return self.data

    def get_data(self, endpoint):
        return self.repository.get_data(endpoint)

