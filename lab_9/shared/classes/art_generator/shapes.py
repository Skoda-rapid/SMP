import math

from shared.classes.art_generator.ascii_art_generator import ArtGenerator


class Shape3D:
    def __init__(self, size=5):
        self.size = size

    def draw(self):
        raise NotImplementedError("Subclasses should implement this!")


class Cube(Shape3D):
    def __init__(self, size=5, symbol="#"):
        super().__init__(size)
        self.symbol = symbol

    def draw(self):
        width = self.size * 2
        height = self.size + 5
        return draw_cube(width, height, self.symbol)


def draw_cube(width, height, symbol):
    cube = [[" "] * width for _ in range(height)]

 
    vertices = {
        "tc": (width // 2, 0),
        "tl": (0, int(0.25 * height)), 
        "tr": (width - 1, int(0.25 * height)),
        "cc": (width // 2, int(0.5 * height)),
        "bl": (0, int(0.75 * height)),
        "br": (width - 1, int(0.75 * height)), 
        "bc": (width // 2, height - 1),
    }

    edges = (
        ("tc", "tl"),
        ("tc", "tr"),
        ("tl", "cc"),
        ("tr", "cc"),
        ("bl", "bc"),
        ("br", "bc"),
        ("cc", "bc"),
    )

    for edge in edges:
        v1 = vertices[edge[0]]
        v2 = vertices[edge[1]]
        x1, y1 = v1
        x2, y2 = v2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        try:
            m = (y2 - y1) / (x2 - x1)
        except ZeroDivisionError:
            for yy in range(min(y1, y2), max(y1, y2) + 1):
                cube[yy][x1] = symbol
        else:
            yy = y1
            for xx in range(x1, x2 + 1):
                cube[int(round(yy))][xx] = symbol
                yy += m

    x1, y1 = vertices["tl"]
    x2, y2 = vertices["bl"]
    for yy in range(min(y1, y2), max(y1, y2) + 1):
        cube[yy][x1] = "|"

    x1, y1 = vertices["tr"]
    x2, y2 = vertices["br"]
    for yy in range(min(y1, y2), max(y1, y2) + 1):
        cube[yy][x1] = "|"

    for xx in range(vertices["tl"][0], vertices["tr"][0] + 1):
        cube[vertices["tc"][1]][xx] = symbol
        cube[vertices["bc"][1]][xx] = symbol

    cube_str = "\n".join("".join(row) for row in cube)
    return cube_str



class Sphere(Shape3D):
    def __init__(self, size, symbol="*", shadow_symbol=".", shadow_offset=2):
        super().__init__(size)
        self.symbol = symbol
        self.shadow_symbol = shadow_symbol
        self.shadow_offset = shadow_offset

    def draw(self):
        output = []
        
        for i in range(-self.size, self.size + 1):
            row = []
            for j in range(-self.size, self.size + 1):
                distance = math.sqrt(i**2 + j**2)
                if distance <= self.size:
                    shadow_intensity = int((distance / self.size) * 10)
                    if shadow_intensity < 4:
                        row.append(self.symbol)
                    else:
                        if j > 0: 
                            row.append(self.shadow_symbol)
                        else:
                            row.append(self.shadow_symbol)
                else:
                    row.append(" ")
            output.append("".join(row).rstrip())

        return "\n".join(output)

class Art3DGenerator(ArtGenerator):
    def __init__(
        self, shape: Shape3D, symbol="*", width=40, height=10, color_mode="bw"
    ):
        super().__init__("", symbol, width, height, "center", color_mode)
        self.shape = shape

    def apply_color(self, text):
        if self.color_mode == "gray":
            return "\033[90m" + text + "\033[0m"
        return text

    def generate_3d_art(self):
        ascii_art = self.apply_color(ascii_art)
        ascii_art = self.shape.draw()
        self.text = ascii_art
        return ascii_art
