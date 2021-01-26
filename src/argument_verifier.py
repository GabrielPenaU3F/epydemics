from src.exceptions.exceptions import InvalidArgumentException


class ArgumentVerifier:

    supported_datasets = ['total_cases', 'total_deaths']

    @classmethod
    def validate_dataset_arguments(cls, country_data, dataset, start, end):
        actual_dataset_end = len(country_data.index) + 1

        cls.validate_dataset(dataset)

        cls.validate_indexes(actual_dataset_end, start, end)

    @classmethod
    def validate_indexes(cls, actual_dataset_end, start_argument, end_argument):
        if start_argument > actual_dataset_end or end_argument > actual_dataset_end:
            raise InvalidArgumentException('Start and end arguments cannot exceed dataset length')

    @classmethod
    def validate_dataset(cls, dataset):
        if dataset not in cls.supported_datasets:
            raise InvalidArgumentException('Supported datasets are total_cases and total_deaths only')

    @classmethod
    def validate_country(cls, data, country_id):
        if country_id not in data['location'].values:
            raise InvalidArgumentException('The requested country is not on the list')
