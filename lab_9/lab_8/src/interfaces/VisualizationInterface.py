
from abc import ABC, abstractmethod

class VisualizationInterface(ABC):
    @abstractmethod
    def visualize(self, data_x, data_y):
        pass
