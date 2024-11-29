import pyfiglet

def choose_font():
    fonts = pyfiglet.FigletFont.getFonts()
    print("Доступні шрифти:", ", ".join(fonts[:10]), "...")
    font = input("Оберіть шрифт для ASCII-арту: ")
    return font if font in fonts else "standard" 
