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

            if end_argument > actual_dataset_end:
                raise InvalidArgumentException('End argument cannot exceed dataset length')
            elif start_argument > end_argument:
                raise InvalidArgumentException('Start argument cannot exceed end argument')

        elif start_argument > actual_dataset_end:
            raise InvalidArgumentException('Start argument cannot exceed dataset length')


    @classmethod
    def validate_dataset(cls, source, dataset):
        supported_datasets = source.get_supported_datasets()
        if dataset not in supported_datasets:
            raise InvalidArgumentException('Requested dataset is not supported')

    @classmethod
    def validate_location(cls, raw_data, location_column_name, location_id):
        current_locations = raw_data[location_column_name].unique().tolist()
        if location_id not in current_locations:
            raise InvalidArgumentException('The requested location was not found')
