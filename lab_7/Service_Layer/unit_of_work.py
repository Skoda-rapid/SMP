class UnitOfWork:
    def __init__(self, history_manager):
        self.history_manager = history_manager
        self._actions = []

    def record_action(self, action):
        self._actions.append(action)

    def commit(self):
        for action in self._actions:
            self.history_manager.record(action)
        self._actions.clear()

    def rollback(self):
        self._actions.clear()
