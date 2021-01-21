from numpy.core.defchararray import strip

from src.domain.sheet import Sheet


class MTBIMinSheet(Sheet):

    def __init__(self, name, data):
        super().__init__(name, data)

    def get_countries(self):
        return strip(self.get_column('Country'))

    def filter_sheet_by_minimum_reached(self):
        filter_obj = filter(lambda row: row[1] == 'TRUE', self.data)
        return list(filter_obj)