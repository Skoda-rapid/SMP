import unittest
from API_Layer.api_client import APIClient
from Repository_Layer.repository import Repository
from Service_Layer.service import DataService
from Persistance_Layer.history import HistoryManager
from input_parser import InputParser
import os
import json

class DataServiceTest(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.repository = Repository(self.api_client)
        self.service = DataService(self.repository)
        self.history = HistoryManager()
    
    def test_get_posts(self):
        posts = self.repository.get_posts()
        self.assertIsInstance(posts, list, "Posts should be returned as a list")
    
    def test_get_users(self):
        users = self.repository.get_users()
        self.assertIsInstance(users, list, "Users should be returned as a list")
    
    def test_list_posts(self):
        self.assertIsNone(self.service.list_posts())

    def test_list_users(self):
        self.assertIsNone(self.service.list_users())

    def test_record_history(self):
        action = "Test Action"
        self.history.record(action)
        with open(self.history.HISTORY_FILE, 'r') as file:
            history = json.load(file)
            self.assertIn(action, history, "Action should be recorded in history")

    def test_show_history(self):
        self.history.record("Another test action")
        history = self.history.show_history()
        self.assertIsNone(history)

    def test_find_dates(self):
        text = "Some random text with date 2023-12-01"
        dates = InputParser.find_dates(text)
        self.assertEqual(dates, ["2023-12-01"], "Date should be extracted correctly")
    
    def test_find_phone_numbers(self):
        text = "Contact number: 123-456-7890"
        phones = InputParser.find_phone_numbers(text)
        self.assertEqual(phones, ["123-456-7890"], "Phone number should be extracted correctly")
    
    def tearDown(self):
        if os.path.exists(self.history.HISTORY_FILE):
            os.remove(self.history.HISTORY_FILE)

if __name__ == '__main__':
    unittest.main()
