# src/data_parser.py
import re

class DataParser:
    def parse_dates(self, text):
        return re.findall(r'\d{4}-\d{2}-\d{2}', text)

    def parse_phones(self, text):
        return re.findall(r'\+?\d[\d\s-]{8,14}\d', text)

    def parse_command(self, command_str: str):
        # A simple implementation of command parsing
        if command_str.lower() == "get posts":
            return "get posts"
        elif command_str.lower() == "get users":
            return "get users"
        elif command_str.lower() == "exit":
            return "exit"
        else:
            return None
