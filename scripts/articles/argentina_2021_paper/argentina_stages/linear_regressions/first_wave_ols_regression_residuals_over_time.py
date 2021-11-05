import numpy as np
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import plot_residual_variances, plot_pvalues, \
    plot_confidence_intervals
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

rsqs = []
residual_vars = []
statistics = []
pvalues = []
confidence_intervals = []

t_axis = np.arange(start_from + m + K, start_from + len(mtbis) - 1)
for t in t_axis:
    mtbis_train = mtbis[0:t - start_from]

    reg = RegressionManager().linear_regression(mtbis_train, m, K, output='full')
    residuals = reg.calculate_residuals()

    r2 = reg.get_r2_score()
    rsqs.append(r2)

    residuals_variance = np.var(residuals, ddof=1)
    residual_vars.append(residuals_variance)

    statistic, pv = test_normality_dagostino_pearson(residuals)
    statistics.append(statistic)
    pvalues.append(pv)

    lim_inf, lim_sup = confidence_interval(residuals, 0.01, 't')
    confidence_intervals.append((lim_inf, lim_sup))

plot_residual_variances(t_axis, residual_vars)
plot_pvalues(t_axis, pvalues, alpha=0.05)
plot_confidence_intervals(t_axis, confidence_intervals, alpha=0.01)
