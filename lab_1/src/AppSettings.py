from colorama import init, Fore

init(autoreset=True)

decimal_places = 2
console_color = Fore.WHITE

def set_decimal(places):
    global decimal_places
    decimal_places = places

def get_decimal():
    return decimal_places

def set_console_color(color):
    global console_color
    color_dict = {
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE
    }
    console_color = color_dict.get(color.lower(), Fore.WHITE)

def get_console_color():
    return console_color
