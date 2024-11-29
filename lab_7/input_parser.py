import re

class InputParser:
    DATE_PATTERN = r'\b\d{2}-\d{2}-\d{4}\b'      # Наприклад, формат YYYY-MM-DD
    PHONE_PATTERN = r'\b\d{3}-\d{3}-\d{4}\b'     # Наприклад, формат XXX-XXX-XXXX

    @staticmethod
    def find_dates(text):
        return re.findall(InputParser.DATE_PATTERN, text)

    @staticmethod
    def find_phone_numbers(text):
        return re.findall(InputParser.PHONE_PATTERN, text)

    @staticmethod
    def parse_input(text):
        dates = InputParser.find_dates(text)
        phones = InputParser.find_phone_numbers(text)
        return {"dates": dates, "phones": phones}
