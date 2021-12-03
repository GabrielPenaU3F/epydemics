import numpy as np

from src.data_manipulation.data_manager import DataManager
from scipy import signal as sg


def get_continent_dataframe(continent):
    DataManager.load_dataset('owid')
    full_continent_df = DataManager.get_data_from_continent(continent)
    return full_continent_df[['location', 'date', 'new_cases', 'new_deaths']]


def get_country_dataframe(country):
    DataManager.load_dataset('owid')
    full_country_df = DataManager.get_data_from_country(country)
    country_df = full_country_df[['date', 'new_cases', 'new_deaths']]
    country_df = country_df[country_df['new_cases'].notna()]
    if not country_df.empty:
        country_df['new_deaths'] = country_df['new_deaths'].fillna(0)
        country_df = country_df.reset_index()
        fix_negatives(country_df)
        return country_df


def split_dataframes_from_continent(continent):
    continent_df = get_continent_dataframe(continent)
    dfs = []
    for country in continent_df['location'].unique():
        country_df = continent_df[continent_df['location'] == country]
        country_df = country_df[country_df['new_cases'].notna()]
        country_df['new_deaths'] = country_df['new_deaths'].fillna(0)
        country_df = country_df.reset_index()
        if not country_df.empty:
            fix_negatives(country_df)
            dfs.append(country_df)

    return dfs


def find_peak_location(data):
    peak_xs, _ = sg.find_peaks(data)
    return peak_xs


def fix_negatives(df):
    for index, row in df.iterrows():
        if row['new_cases'] < 0:
            df['new_cases'].loc[index] = (df['new_cases'].loc[index - 1] + df['new_cases'].loc[index + 1])/2

        if row['new_deaths'] < 0:
            df['new_deaths'].loc[index] = (df['new_deaths'].loc[index - 1] + df['new_deaths'].loc[index + 1]) / 2
