import pyexcel_io

from domain.mtbi_min_sheet import MTBIMinSheet
from domain.sheet import Sheet


class SpreadsheetDataManager:

    def __init__(self, path, **kwargs):
        self.file = pyexcel_io.get_data(path)
        self.sheets = self.build_sheets(kwargs['type'])

    def get_sheet(self, name):
        return self.sheets[name]

    def build_sheets(self, type):
        sheets = {}
        for sheet_name in self.file.keys():
            file_sheet = self.file[sheet_name]
            if type == 'mtbi_min':
                sheets[sheet_name] = self.build_mtbi_min_sheet(sheet_name, file_sheet)
            else:
                sheets[sheet_name] = self.build_regular_sheet(sheet_name, file_sheet)
        return sheets

    def build_regular_sheet(self, sheet_name, file_sheet):
        return Sheet(sheet_name, file_sheet)

    def build_mtbi_min_sheet(self, sheet_name, file_sheet):
        return MTBIMinSheet(sheet_name, file_sheet)
