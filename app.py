from config import SPREADSHEET_ID, SHEET_NAME, SHEET_ID
from logic import SpreadsheetAPI

# файл является точкой входа в программу


if __name__ == '__main__':
    api = SpreadsheetAPI(SPREADSHEET_ID, SHEET_NAME, SHEET_ID)
    api.insert("A1:B2", [["A1", "A2"], ["B1", "B2"]])
    print(api.get_sheet())
    print(api.get("A1:A2"))
    api.full_clear()
    print(api.get_sheet())
