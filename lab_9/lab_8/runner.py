
from src.main import main
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
sys.path.append(project_root)

if __name__ == "__main__":
    main()
