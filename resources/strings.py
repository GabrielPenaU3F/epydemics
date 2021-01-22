class StringManager:

    dataset_title_strings = {
        'total_cases': 'Cases in ',
        'total_deaths': 'Deaths in '
    }

    @classmethod
    def get_dataset_title(cls, key):
        return cls.dataset_title_strings.get(key)
