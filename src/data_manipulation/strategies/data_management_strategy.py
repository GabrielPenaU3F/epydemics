from abc import ABC, abstractmethod

from src.data_manipulation.dataframe_slicer import DataframeSlicer


class DataManagementStrategy(ABC):

    @abstractmethod
    def get_location_list(self, raw_data):
        pass

    def filter_rows(self, data, dataset_column, start, end):
        return DataframeSlicer.slice_rows_by_index(data, start, end)


class OWIDManagementStrategy(DataManagementStrategy):

    def get_location_list(self, raw_data):
        return raw_data['location'].unique()


class MapacheArgManagementStrategy(DataManagementStrategy):

    def get_location_list(self, raw_data):
        return raw_data['osm_admin_level_4'].unique()

    def filter_rows(self, data, dataset_column, start, end):
        data[dataset_column] = data[dataset_column].cumsum(axis=None)
        return super().filter_rows(data, dataset_column, start, end)


class CustomManagementStrategy(DataManagementStrategy):

    def get_location_list(self, raw_data):
        return raw_data['custom_location'].unique()
