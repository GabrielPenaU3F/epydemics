from resources.strings import TotalCasesStrings, TotalDeathsStrings


class StringManager:

    dataset_strings = {
        'total_cases': TotalCasesStrings(),
        'total_deaths': TotalDeathsStrings()
    }

    @classmethod
    def get_dataset_title(cls, key):
        return cls.dataset_strings.get(key).get_dataset_title()

    @classmethod
    def get_dataset_column_title(cls, key):
        return cls.dataset_strings.get(key).get_dataset_column_title()

    @classmethod
    def get_fit_plot_ylabel(cls, key):
        return cls.dataset_strings.get(key).get_dataset_plot_ylabel()
