import pandas as pd
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LoadDataCommand(Command):
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def execute(self):
        self.data = pd.read_csv(self.filename, delimiter=';')
        return self.data

class ExtremeValuesCommand(Command):
    def __init__(self, data):
        self.data = data
        self.extreme_values = None

    def execute(self):
        self.extreme_values = self.data.describe()
        return self.extreme_values

    def undo(self):
        self.extreme_values = None