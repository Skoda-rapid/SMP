from UI.handle_input import write_to_output

class ConsoleWriter:
    def output_value(self, value, message="Ваше значення"):
        write_to_output(f"{message}: {value}")