#shared\functions\ui_functions\handle_input.py

def read_from_input(message=""):
    return input(message)

def write_to_output(value, message="Ваше значення:"):
    print(f'{message}: {value}')
