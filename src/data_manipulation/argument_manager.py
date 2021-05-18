from src.exceptions.exceptions import InvalidArgumentException


class ArgumentManager:

    @classmethod
    def validate_dataset_arguments(cls, source, location_data, dataset, start, end):
        actual_dataset_end = len(location_data.index) + 1

        cls.validate_dataset(source, dataset)

        cls.validate_indexes(actual_dataset_end, start, end)

    @classmethod
    def validate_indexes(cls, actual_dataset_end, start_argument, end_argument):
        if end_argument is not None:
            if start_argument > actual_dataset_end or end_argument > actual_dataset_end:
                raise InvalidArgumentException('Start and end arguments cannot exceed dataset length')

    @classmethod
    def validate_dataset(cls, source, dataset):
        supported_datasets = source.get_supported_datasets()
        if dataset not in supported_datasets:
            raise InvalidArgumentException('Requested dataset is not supported')

    @classmethod
    def validate_location(cls, raw_data, location_column_name, location_id):
        if location_id not in raw_data[location_column_name].unique():
            raise InvalidArgumentException('The requested location was not found')

    @classmethod
    def determine_start_from(cls, start, start_from):

        if start_from < start and start_from != -1:
            raise InvalidArgumentException('start_from argument must not exceed start argument')

        if start == 1:
            if start_from == -1:
                return 30
            else:
                return start_from
        elif start > 1:
            if start_from == -1:
                return start + 30
            else:
                return start_from


