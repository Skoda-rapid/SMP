from colorama import init

init(autoreset=True)

decimal_places = 2
console_color = "\x1b[37m"


def set_decimal(places):
    global decimal_places
    decimal_places = places


def get_decimal():
    return decimal_places


colors = {
    "black": "\x1b[30m",
    "red": "\x1b[31m",
    "green": "\x1b[32m",
    "yellow": "\x1b[33m",
    "blue": "\x1b[34m",
    "magenta": "\x1b[35m",
    "cyan": "\x1b[36m",
    "white": "\x1b[37m",
    "reset": "\x1b[0m",
}


def set_console_color(color):

    global console_color
    console_color = colors[color]


def get_console_color():
    return console_color
