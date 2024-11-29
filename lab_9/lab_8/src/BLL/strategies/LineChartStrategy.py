
import matplotlib.pyplot as plt
from ...interfaces.VisualizationInterface import VisualizationInterface

class LineChartStrategy(VisualizationInterface):
    def visualize(self, data_x, data_y):
        if not data_x or not data_y or len(data_x) != len(data_y):
            raise ValueError("Помилка: Дані для графіка некоректні.")
        
        plt.plot(data_x, data_y, label="Лінійний графік")
        plt.xlabel("X (вісь)")
        plt.ylabel("Y (вісь)")
        plt.title("Лінійний графік даних")
        plt.legend()
        plt.show()
