import numpy as np

from scripts.articles.argentina_2021_paper.useful_functions import show_regression_coefficients
from scripts.experiments.mtbi_multiple_linear_regressions.utils import scatterplot_m_K, heatmap, coef_barplot
from src.data_manipulation.data_manager import DataManager
from src.domain.regression_manager import RegressionManager
from src.interface import epydemics as ep

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start = 1
end = 229
start_from = 30

mtbis = np.array(ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                 start_from=start_from, output=False, formula='approx_conditional'))

mtbis_train = mtbis[:69]

# -----------------
real_mtbi = mtbis[69]

reg = RegressionManager().linear_regression(mtbis_train, 25, 8, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
coefficients = [coef for coef in reg.get_coefficients()][1:]
print('m=25, K=8 - Relative error: ' + str(rel_err) + '%')
show_regression_coefficients(coefficients)
