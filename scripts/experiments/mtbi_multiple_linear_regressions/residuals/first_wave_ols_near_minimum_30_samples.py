import numpy as np

from scripts.experiments.mtbi_multiple_linear_regressions.utils import scatterplot_m_K, heatmap, coef_barplot, \
    test_normality_dagostino_pearson, test_normality_lilliefors
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

# -----------------
real_mtbi = mtbis[len(mtbis) - 1]

reg = RegressionManager().linear_regression(mtbis_train, 30, 6, output='full', affine=False)
residuals = reg.calculate_residuals()
r2 = reg.get_r2_score()
print(r2)
print(residuals)

print('\n')
print('Residuals mean: ' + str(np.mean(residuals)))
print('Residuals sample variance: ' + str(np.var(residuals, ddof=1)))

print('\nD Agostino - Pearson normality test')
statistic, pv = test_normality_dagostino_pearson(residuals)
print('Statistic: ' + str(statistic))
print('p-value: ' + str(pv))

print('\nLilliefors (Kolmogorov-Smirnov) test for normal goodness of fit')
statistic, pv = test_normality_lilliefors(residuals)
print('Statistic: ' + str(statistic))
print('p-value: ' + str(pv))
