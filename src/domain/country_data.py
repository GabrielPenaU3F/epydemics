import numpy as np

from src.correctors.relative_difference_corrector import RelativeDifferenceCorrector
from src.console_displayer import ConsoleDisplayer

from src.string_formater import format_title


class CountryData:

    rows = None
    rows_backup = None

    def __init__(self, country_id, raw_data):

        self.rows = dict()
        self.rows_backup = dict()

        dataset_beginning = self.determine_dataset_beginning(raw_data)
        days = np.array(raw_data.index.tolist()[dataset_beginning:len(raw_data)], copy=True) + 1 - dataset_beginning
        values = np.array(raw_data.values.tolist()[dataset_beginning:len(raw_data)], copy=True)
        for i in range(len(days)):
            self.rows[days[i]] = values[i]
        self.rows_backup = self.rows.copy()

        self.country_name = format_title(country_id)
        self.console_displayer = ConsoleDisplayer(self.get_country_name())

    def get_value(self, day):
        return self.rows.get(day)

    def delete_value(self, day):
        self.rows.pop(day)

    def delete_nans(self):
        for k in range(len(self.rows)):
            if np.isnan(self.rows[k + 1]):
                self.delete_value(k + 1)

    def locf_nans(self):
        for k in range(2, len(self.rows) + 1):
            if np.isnan(self.rows.get(k)):
                self.rows[k] = self.rows[k - 1]

    def restore_original_data(self):
        self.rows = self.rows_backup.copy()

    def print(self):
        self.console_displayer.print(list(self.rows.keys()), list(self.rows.values()))

    def get_days(self):
        return np.array(list(self.rows.keys()))

    def get_values(self):
        return np.array(list(self.rows.values()))

    def get_country_name(self):
        return self.country_name

    def apply_relative_difference_correction(self, constant_days, constant_tolerance, jump_tolerance):
        corrector = RelativeDifferenceCorrector(constant_days, constant_tolerance, jump_tolerance)
        new_values = corrector.correct_data(self.get_values())
        self.update_values(new_values)

    def determine_dataset_beginning(self, raw_data):
        first_nonnan = raw_data.first_valid_index()
        for i in range(first_nonnan, len(raw_data)):
            if raw_data.get(i) > 0:
                return i

    def update_values(self, new_values):
        keys = list(self.rows.keys())
        for i in range(len(new_values)):
            self.rows[keys[i]] = new_values[i]
