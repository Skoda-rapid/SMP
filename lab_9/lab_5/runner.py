import sys
import os

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, lab5_root)

# src_path = os.path.join(project_root, "lab_5", "src")
# sys.path.insert(0, src_path)

from main import main

if __name__ == "__main__":
    main()
