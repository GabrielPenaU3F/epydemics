import pandas

from domain.country_data import CountryData


class URLDataManager:

    def __init__(self, url):
        self.data = pandas.read_csv(url)

    def get_cases_from_country(self, country_id):
        raw_data = self.data[country_id]
        return CountryData(country_id, raw_data)
