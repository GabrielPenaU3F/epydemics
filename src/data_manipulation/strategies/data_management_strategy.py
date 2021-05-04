from abc import ABC, abstractmethod

import numpy as np

from src.data_manipulation.dataframe_slicer import DataframeSlicer


class DataManagementStrategy(ABC):

    @abstractmethod
    def get_location_list(self, raw_data):
        pass

    def filter_rows(self, data, dataset_column, start, end):
        requested_subset = DataframeSlicer.slice_rows_by_index(data, start, end)
        accumulated_events_previous_to_start = 0
        if start > 1:
            accumulated_events_previous_to_start = data[dataset_column].iloc[start - 2]
        requested_subset.loc[:, dataset_column] -= accumulated_events_previous_to_start
        return requested_subset


class OWIDManagementStrategy(DataManagementStrategy):

    def get_location_list(self, raw_data):
        return raw_data['location'].unique()


class MapacheArgManagementStrategy(DataManagementStrategy):

    def get_location_list(self, raw_data):
        return raw_data['osm_admin_level_4'].unique()

    def filter_rows(self, data, dataset_column, start, end):
        data[dataset_column] = data[dataset_column].cumsum(axis=None)
        return super().filter_rows(data, dataset_column, start, end)
