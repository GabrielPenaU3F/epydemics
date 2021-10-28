import numpy as np

from scripts.experiments.mtbi_multiple_linear_regressions.utils import scatterplot_m_K, heatmap, coef_barplot
from src.data_manipulation.data_manager import DataManager
from src.domain.regression_manager import RegressionManager
from src.interface import epydemics as ep

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start = 351
end = 412
start_from = 20

mtbis = np.array(ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                 start_from=start_from, output=False, formula='approx_conditional'))

mtbis_train = mtbis[:-1]

# -----------------
real_mtbi = mtbis[len(mtbis) - 1]

print('Experiment 7.0: Ordinary least squares - Real MTBI = ' + str(round(real_mtbi, 4)) + '\n')

points = []

# m = 15
print('\n')

reg = RegressionManager().linear_regression(mtbis_train, 15, 8, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
coef_barplot(coefficients)

reg = RegressionManager().linear_regression(mtbis_train, 15, 6, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().linear_regression(mtbis_train, 15, 4, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().linear_regression(mtbis_train, 15, 2, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 7
print('\n')

reg = RegressionManager().linear_regression(mtbis_train, 7, 8, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().linear_regression(mtbis_train, 7, 6, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().linear_regression(mtbis_train, 7, 4, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().linear_regression(mtbis_train, 7, 2, output='full', affine=False)
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

points = np.array(points)

heatmap(points, 'Relative error (%)')

