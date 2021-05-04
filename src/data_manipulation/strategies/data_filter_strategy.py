from abc import ABC, abstractmethod


class DataFilterStrategy(ABC):

    @abstractmethod
    def get_location_list(self, raw_data):
        pass


class OWIDFilterStrategy(DataFilterStrategy):

    def get_location_list(self, raw_data):
        return raw_data['location'].unique()


class MapacheArgFilterStrategy(DataFilterStrategy):

    def get_location_list(self, raw_data):
        return raw_data['osm_admin_level_4'].unique()
