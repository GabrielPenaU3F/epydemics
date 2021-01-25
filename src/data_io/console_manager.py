import pandas

from src.strings_manager import StringManager


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

    def print_data_from_country(self, country_dataframe, country, dataset_type):
        printable_df = country_dataframe.copy()
        date_column_title = 'Date'
        dataset_column_title = StringManager.get_dataset_column_title(dataset_type)
        printable_df.columns = [date_column_title, dataset_column_title]
        print('\n-----------------------')
        print(StringManager.get_dataset_title(dataset_type) + country)
        print('-----------------------')
        print(printable_df)
        print('-----------------------')

    def show_fit_results(self, fit):
        print('\n-----------------------')
        print(StringManager.get_dataset_title(fit.get_dataset_type()) + fit.get_country())
        print('-----------------------')
        print('Model parameters:')
        print('\u03C1 (1/day):  ' + str(fit.get_params()[0]))
        print('\u03B3 / \u03C1:  ' + str(fit.get_params()[1]))
        print('-----------------------')
        print('Goodness of fit:')
        print('R2:  ' + str(fit.get_rsq()))
        print('-----------------------')
