
from abc import ABC, abstractmethod


class VisualizationStrategy(ABC):

    @abstractmethod
    def visualize(self):
        pass
