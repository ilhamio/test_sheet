import unittest

from config import SPREADSHEET_ID, SHEET_NAME, SHEET_ID
from logic import SpreadsheetAPI


class TestSpreadsheetAPI(unittest.TestCase):
    def setUp(self):
        self.api = SpreadsheetAPI(SPREADSHEET_ID, SHEET_NAME, SHEET_ID)
        self.api.full_clear()

    def tearDown(self) -> None:
        self.api.full_clear()

    def test_insert(self):
        self.api.insert("A1:B2", [["A1", "A2"], ["B1", "B2"]])
        self.assertEqual(self.api.get_sheet(),
                         {'majorDimension': 'ROWS', 'range': 'main!A1:Z1000', 'values': [['A1', 'A2'], ['B1', 'B2']]})

    def test_clear(self):
        self.assertEqual(self.api.full_clear(),
                         {'majorDimension': 'ROWS', 'range': 'main!A1:Z1000'})

