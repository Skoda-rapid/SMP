import pyfiglet
from termcolor import colored

def scale_ascii_art(ascii_art, scale):
    lines = ascii_art.splitlines()
    scaled_lines = []
    for line in lines:
        scaled_line = "".join([char * scale for char in line])
        for _ in range(scale):
            scaled_lines.append(scaled_line)
    return "\n".join(scaled_lines)

def generate_ascii_art(text, font, color, symbol="#", width=None, scale=1):
    if width is None:
        width = 80

    ascii_art = pyfiglet.figlet_format(text, font=font, width=width)
    if symbol:
         for char in ascii_art:
            if char != '\n' and char != ' ':
              ascii_art = ascii_art.replace(char, symbol)


    if scale > 1:
        ascii_art = scale_ascii_art(ascii_art, scale)

    colored_ascii_art = colored(ascii_art, color)
    return colored_ascii_art
