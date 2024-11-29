"""
Модуль `runner.py` для запуску лабораторних робіт.

Містить головну функцію для виклику меню і запуску обраної лабораторної роботи.
"""

import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_path)

from src.main import main

if __name__ == "__main__":
    main()
