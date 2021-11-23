import numpy as np
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import plot_residual_variances, plot_pvalues, \
    plot_confidence_intervals, plot_mtbi_prediction_errors, plot_cases_prediction_errors
from scripts.experiments.mtbi_multiple_linear_regressions.utils import scatterplot_m_K, heatmap, coef_barplot, \
    test_normality_dagostino_pearson, test_normality_lilliefors, confidence_interval
from src.data_manipulation.data_manager import DataManager
from src.domain.regression_manager import RegressionManager
from src.domain.unit_converter import DaysConverter
from src.interface import epydemics as ep

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start = 1
end = 229
start_from = 30

mtbis = np.array(ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                 start_from=start_from, output=False, formula='approx_conditional'))
mtbis_train = mtbis[:199]

# Model parameters
m = 25
K = 8

real_cases = DataManager.get_raw_daily_data('Argentina', start=start + start_from, end=end)
mtbi_prediction_errors = []
cases_prediction_errors = []
t_axis = np.arange(start_from + m + K, start_from + len(mtbis) - 1)

for t in t_axis:
    t_actual = t - start_from
    mtbis_train = mtbis[0:t_actual]

    reg = RegressionManager().linear_regression(mtbis_train, m, K, output='full')
    predicted_mtbi = reg.predict()
    err = abs(mtbis[t_actual] - predicted_mtbi) / mtbis[t_actual]
    mtbi_prediction_errors.append(err)

    predicted_cases = 1 / (mtbis[t_actual] / 86400)
    cases_err = abs(real_cases[t_actual] - predicted_cases) / real_cases[t_actual]
    cases_prediction_errors.append(cases_err)

print('Mean: ' + str(np.mean(mtbi_prediction_errors)))
print('Variance: ' + str(np.var(mtbi_prediction_errors, ddof=1)))
plot_mtbi_prediction_errors(t_axis, mtbi_prediction_errors)
plot_cases_prediction_errors(t_axis, cases_prediction_errors)
