import pandas


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
        date_column_title = 'Date'
        dataset_column_title = source.get_dataset_title(dataset)
        location_dataframe.columns = [date_column_title, dataset_column_title]
        print('\n-----------------------')
        print(source.get_dataset_title(dataset) + ' in ' + location_id)
        print('-----------------------')
        print(location_dataframe)
        print('-----------------------')

    def show_fit_results(self, fit):
        source = fit.get_source()
        print('\n-----------------------')
        print(source.get_dataset_title(fit.get_dataset_type()) + fit.get_location())
        print('-----------------------')
        print('Model parameters:')
        print('\u03C1 (1/day):  ' + str(fit.get_params()[0]))
        print('\u03B3 / \u03C1:  ' + str(fit.get_params()[1]))
        print('-----------------------')
        print('Goodness of fit:')
        print('R2:  ' + str(fit.get_rsq()))
        print('-----------------------')
