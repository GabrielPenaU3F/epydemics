from abc import ABC


class DatasetStrings(ABC):

    dataset_title = None
    dataset_column_title = None
    plot_ylabel = None

    def get_dataset_title(self):
        return self.dataset_title

    def get_dataset_column_title(self):
        return self.dataset_column_title

    def get_dataset_plot_ylabel(self):
        return self.plot_ylabel


class TotalCasesStrings(DatasetStrings):

    def __init__(self):
        self.dataset_title = 'Cases in '
        self.dataset_column_title = 'Total cases'
        self.plot_ylabel = 'Cumulative cases'


class TotalDeathsStrings(DatasetStrings):

    def __init__(self):
        self.dataset_title = 'Deaths in '
        self.dataset_column_title = 'Total deaths'
        self.plot_ylabel = 'Cumulative deaths'
