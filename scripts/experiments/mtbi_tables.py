import numpy as np

from src.data_io.data_writer import DataWriter
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep
import pandas as pd


output_path = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/mtbi_table.csv'
DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 30
start = 1
end = 229

mtbis = np.array(ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                 start_from=start_from, output=False, formula='approx_conditional'))

mtbis_series = pd.Series(mtbis)

DataWriter.write_to_csv(mtbis_series, output_path)
