import numpy as np

from src.data_manipulation.data_manager import DataManager
from src.domain.regression_manager import RegressionManager
from src.interface import epydemics as ep

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 30
start = 1
end = 229

segment_start = 120
segment_end = 199

mtbis = np.array(ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                 start_from=start_from, output=False, formula='approx_conditional'))
mtbis_train = mtbis[segment_start:segment_end]

m = 15
K = 8
reg = RegressionManager().linear_regression(mtbis, m, K, output='full')

print('Real MTBI: ' + str(mtbis[199]))
print('Predicted MTBI: ' + str(reg.predict()))
