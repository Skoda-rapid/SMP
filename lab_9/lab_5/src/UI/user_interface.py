import os
import sys

# project_root = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "..", "..", "..")
# )
# if project_root not in sys.path:
#     sys.path.insert(0, os.path.join(project_root, "shared"))

from ..BLL.art_manager import ArtManager
from shared.classes.art_generator.console_reader import ConsoleReader


class UserInterface:
    def start(self):
        print("Welcome to the ASCII Art 3D Generator!")

        art_type = ConsoleReader.read_art_type()

        art_manager = ArtManager()

        if art_type == "text":
            params = ConsoleReader.read_text_parameters()
            art_instance = art_manager.create_text_art(params)
        elif art_type == "shape":
            params = ConsoleReader.read_shape_parameters()
            art_instance = art_manager.create_shape(
                params["shape_type"], params["size"], params["symbol"]
            )

        art = art_manager.generate_art(art_instance)

        print("\nGenerated ASCII Art:\n")
        print(art)
