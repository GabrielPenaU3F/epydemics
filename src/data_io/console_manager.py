import numpy as np
import pandas
import src.utils.checking_utils as checker
from src.data_manipulation.data_manager import DataManager
from src.domain.unit_converter import DaysConverter


class ConsoleManager:

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ConsoleManager()
        return cls.instance

    def __init__(self):
        self.configure_dataframe_prints()

    def configure_dataframe_prints(self):
        pandas.set_option("display.max_rows", None, "display.max_columns", None)

    def print_locations(self, locations):
        print("List of available locations:")
        print(locations)

    def print_data_from_location(self, source, location_id, dataset, location_dataframe):
        dataset = DataManager.choose_dataset(dataset)
        date_column_title = 'Date'
        dataset_column_title = source.get_dataset_title(dataset)
        location_dataframe.columns = [date_column_title, dataset_column_title]
        print('\n-----------------------')
        print(source.get_dataset_title(dataset) + ' in ' + location_id)
        print('-----------------------')
        print(location_dataframe)
        print('-----------------------')

    def show_fit_results(self, fit, location, dataset):
        source = DataManager.get_data_source()
        dataset = DataManager.choose_dataset(dataset)
        print('\n-----------------------')
        print(source.get_dataset_title(dataset) + ' in ' +
              location)
        print('-----------------------')
        print('Model parameters:')
        print('\u03C1 (1/day):  ' + str(fit.get_params()[0]))
        print('\u03B3 / \u03C1:  ' + str(fit.get_params()[1]))
        print('-----------------------')
        print('Goodness of fit_model:')
        print('R2:  ' + str(fit.get_rsq()))
        print('-----------------------')

    def show_minimum_status(self, mtbis, start_from, unit):
        mtbis = DaysConverter.get_instance().convert_days_to(unit, mtbis)
        if checker.check_if_minimum_was_reached(mtbis):
            status = 'REACHED'
        else:
            status = 'NOT REACHED'
        print('\n-----------------------')
        print('Minimum status: ' + status)
        print('Current minimum is ' +
              str(np.min(mtbis)) + ' ' + unit + ', located at day ' + str(np.argmin(mtbis) + start_from + 1))
        print('-----------------------')
