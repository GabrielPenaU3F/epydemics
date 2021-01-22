from abc import ABC


class DatasetStrings(ABC):

    dataset_title = None
    plot_ylabel = None

    def get_dataset_title(self):
        return self.dataset_title

    def get_dataset_plot_ylabel(self):
        return self.plot_ylabel


class TotalCasesStrings(DatasetStrings):

    def __init__(self):
        self.dataset_title = 'Cases in '
        self.plot_ylabel = 'Cumulative cases'


class TotalDeathsStrings(DatasetStrings):

    def __init__(self):
        self.dataset_title = 'Deaths in '
        self.plot_ylabel = 'Cumulative deaths'
