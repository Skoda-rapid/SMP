history = []

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def show_history():
    if not history:
        print("Обчислення відсутні.")
    else:
        for record in history:
            print(record)
