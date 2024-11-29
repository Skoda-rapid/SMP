# src/BLL/factories/VisualizationFactory.py

import os
import sys

lab8_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
sys.path.append(lab8_root)

from lab_8.src.interfaces import VisualizationInterface
from ...BLL.strategies.LineChartStrategy import LineChartStrategy
from ...BLL.strategies.BarChartStrategy import BarChartStrategy


class VisualizationFactory:
    def get_visualization_strategy(self, choice: str):
        match choice:
            case "1":
                return LineChartStrategy()
            case "2":
                return BarChartStrategy()
            case _:
                raise ValueError("Невідомий вибір стратегії візуалізації")

    def create_strategy(self, choice: str) -> VisualizationInterface:
          match choice:
              case "line":
                  return LineChartStrategy()
              case "bar":
                  return BarChartStrategy()
              case _:
                  raise ValueError("Невідомий вибір стратегії візуалізації")