from src.exceptions.exceptions import InvalidArgumentException


class ArgumentVerifier:

    @classmethod
    def validate_dataset_arguments(cls, source, location_data, dataset, start, end):
        actual_dataset_end = len(location_data.index) + 1

        cls.validate_dataset(source, dataset)

        cls.validate_indexes(actual_dataset_end, start, end)

    @classmethod
    def validate_indexes(cls, actual_dataset_end, start_argument, end_argument):
        if start_argument > actual_dataset_end or end_argument > actual_dataset_end:
            raise InvalidArgumentException('Start and end arguments cannot exceed dataset length')

    @classmethod
    def validate_dataset(cls, source, dataset):
        supported_datasets = source.get_supported_datasets()
        if dataset not in supported_datasets:
            raise InvalidArgumentException('Supported datasets are total_cases and total_deaths only')

    @classmethod
    def validate_location(cls, raw_data, location_column_name, location_id):
        if location_id not in raw_data[location_column_name].unique():
            raise InvalidArgumentException('The requested location was not found')
