import numpy as np
from matplotlib import pyplot as plt

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

t_axis = np.arange(m + K, len(mtbis) - 1)
for t in t_axis:
    mtbis_train = mtbis[0:t]

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

plt.tick_params(axis='both', which='major', labelsize=18)

# plt.plot(t_axis, rsqs, label='r2')
# plt.legend(fontsize=32)
# plt.show()
#
# plt.plot(t_axis, residual_vars, label='Variance of the residuals')
# plt.legend(fontsize=32)
# plt.show()
#
# plt.plot(t_axis, statistics, label='D\'Agostino - Pearson statistic')
# plt.legend(fontsize=32)
# plt.show()
#
# significance_line = np.full_like(t_axis, 0.05, dtype=np.double)
# plt.plot(t_axis, pvalues, label='D\'Agostino - Pearson test p-value')
# plt.plot(t_axis, significance_line, color='red', linestyle='--', linewidth=0.5, label='0.05 significance level')
# plt.legend(fontsize=32)
# plt.show()

lim_infs = [interval[0] for interval in confidence_intervals]
lim_sups = [interval[1] for interval in confidence_intervals]
plt.fill_between(x=t_axis, y1=lim_infs, y2=lim_sups, alpha=0.5, color='blue')
plt.show()
