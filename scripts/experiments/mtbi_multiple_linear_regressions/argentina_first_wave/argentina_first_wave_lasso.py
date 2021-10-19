import numpy as np

from scripts.experiments.mtbi_multiple_linear_regressions.utils import heatmap
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

mtbis_train = mtbis[120:199]

# -----------------
real_mtbi = mtbis[199]

points = []

# print('Experiment 1.10: Lasso regression (\u03B1 = 0.4) - Real MTBI = ' + str(round(mtbis[199], 4)) + '\n')
#
# # m = 30
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 16, alpha=0.4, output='full')
# print('m=30, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 8, alpha=0.4, output='full')
# print('m=30, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 6, alpha=0.4, output='full')
# print('m=30, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 4, alpha=0.4, output='full')
# print('m=30, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 2, alpha=0.4, output='full')
# print('m=30, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# # m = 15
# print('\n')
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 16, alpha=0.4, output='full')
# print('m=15, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 8, alpha=0.4, output='full')
# print('m=15, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 6, alpha=0.4, output='full')
# print('m=15, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 4, alpha=0.4, output='full')
# print('m=15, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 2, alpha=0.4, output='full')
# print('m=15, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# # m = 7
# print('\n')
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 16, alpha=0.4, output='full')
# print('m=7, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 8, alpha=0.4, output='full')
# print('m=7, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 6, alpha=0.4, output='full')
# print('m=7, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 4, alpha=0.4, output='full')
# print('m=7, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 2, alpha=0.4, output='full')
# print('m=7, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# --------------------

# print('Experiment 1.11: Lasso regression (\u03B1 = 0.1) - Real MTBI = ' + str(round(mtbis[199], 4)) + '\n')
#
# # m = 30
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 16, alpha=0.1, output='full')
# print('m=30, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 8, alpha=0.1, output='full')
# print('m=30, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 6, alpha=0.1, output='full')
# print('m=30, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 4, alpha=0.1, output='full')
# print('m=30, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 30, 2, alpha=0.1, output='full')
# print('m=30, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# # m = 15
# print('\n')
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 16, alpha=0.1, output='full')
# print('m=15, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 8, alpha=0.1, output='full')
# print('m=15, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 6, alpha=0.1, output='full')
# print('m=15, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 4, alpha=0.1, output='full')
# print('m=15, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 15, 2, alpha=0.1, output='full')
# print('m=15, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# # m = 7
# print('\n')
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 16, alpha=0.1, output='full')
# print('m=7, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 8, alpha=0.1, output='full')
# print('m=7, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 6, alpha=0.1, output='full')
# print('m=7, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 4, alpha=0.1, output='full')
# print('m=7, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
#
# reg = RegressionManager().lasso_regression(mtbis, 7, 2, alpha=0.1, output='full')
# print('m=7, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# ---------------

print('Experiment 1.12: Lasso regression (\u03B1 = 0.01) - Real MTBI = ' + str(round(mtbis[199], 4)) + '\n')

# m = 30

reg = RegressionManager().lasso_regression(mtbis, 30, 16, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 30, 8, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 30, 6, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 30, 4, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 30, 2, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 15
print('\n')

reg = RegressionManager().lasso_regression(mtbis, 15, 16, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 15, 8, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 15, 6, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 15, 4, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 15, 2, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 7
print('\n')

reg = RegressionManager().lasso_regression(mtbis, 7, 16, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 7, 8, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 7, 6, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 7, 4, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().lasso_regression(mtbis, 7, 2, alpha=0.01, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

points = np.array(points)
heatmap(points, 'Relative error (%)')
