import unittest
import os
import sys

lab7_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(lab7_root)

from ..DAL.api_repository import APIRepository
from lab_7.src.BLL.unit_of_work import UnitOfWork
from ..UI.user_input_parser import UserInputParser
from ..BLL.history_manager import HistoryManager


class TestAPIRepository(unittest.TestCase):
    def setUp(self):
        self.repo = APIRepository("https://jsonplaceholder.typicode.com")

    def test_get_data_posts(self):
        data = self.repo.get_data("posts")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_get_data_users(self):
        data = self.repo.get_data("users")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)


class TestUnitOfWork(unittest.TestCase):
    def setUp(self):
        repo = APIRepository("https://jsonplaceholder.typicode.com")
        self.uow = UnitOfWork(repo)

    def test_get_data(self):
        data = self.uow.get_data("posts")
        self.assertIsInstance(data, list)


class TestUserInputParser(unittest.TestCase):
    def setUp(self):
        self.parser = UserInputParser()

    def test_parse_command_valid(self):
        command = self.parser.parse_command("get posts")
        self.assertEqual(command, "get posts")

    def test_parse_command_invalid(self):
        command = self.parser.parse_command("unknown command")
        self.assertIsNone(command)


class TestHistoryManager(unittest.TestCase):
    def setUp(self):
        self.history_manager = HistoryManager("test_history.json")

    def test_save_and_load_history(self):
        test_data = {"command": "get posts", "data": [{"id": 1, "title": "Test Post"}]}
        self.history_manager.save_to_history(test_data["command"], test_data["data"])

        history = self.history_manager.load_history()
        self.assertGreater(len(history), 0)
        self.assertEqual(history[-1]["command"], "get posts")
        self.assertEqual(history[-1]["data"], test_data["data"])

    def tearDown(self):
        # Видалення тестового файлу історії після тестування
        if os.path.exists("test_history.json"):
            os.remove("test_history.json")


if __name__ == "__main__":
    unittest.main()
