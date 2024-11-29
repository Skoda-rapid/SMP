# src/user_input_parser.py
class UserInputParser:
    def parse_command(self, user_input):
        valid_commands = ["get posts", "get users", "exit"]
        return user_input.strip() if user_input.strip() in valid_commands else None
