# runner.py
import os
import sys

from src.main import main

lab4_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab4_root)

if __name__ == "__main__":
    main()
