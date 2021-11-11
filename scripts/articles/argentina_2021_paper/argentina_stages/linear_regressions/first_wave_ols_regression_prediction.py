import numpy as np
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import plot_residual_variances, plot_pvalues, \
    plot_confidence_intervals, plot_prediction_errors
from scripts.experiments.mtbi_multiple_linear_regressions.utils import scatterplot_m_K, heatmap, coef_barplot, \
    test_normality_dagostino_pearson, test_normality_lilliefors, confidence_interval
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

mtbis_train = mtbis[:199]

# Model parameters
m = 25
K = 8

prediction_errors = []
t_axis = np.arange(start_from + m + K, start_from + len(mtbis) - 1)

for t in t_axis:
    t_actual = t - start_from
    mtbis_train = mtbis[0:t_actual]
    reg = RegressionManager().linear_regression(mtbis_train, m, K, output='full')
    err = abs(mtbis[t_actual] - reg.predict()) / mtbis[t_actual]
    prediction_errors.append(err)

print('Mean: ' + str(np.mean(prediction_errors)))
print('Variance: ' + str(np.var(prediction_errors, ddof=1)))
plot_prediction_errors(t_axis, prediction_errors)

