import numpy as np

from scripts.experiments.mtbi_multiple_linear_regressions.utils import three_heatmaps, coef_barplot
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
alpha_1 = 0.4
print('\n Experiment 1.2: Ridge regression (\u03B1 = ' + str(alpha_1) + ') - Real MTBI = ' + str(round(real_mtbi, 4)) + '\n')

# m = 30

reg = RegressionManager().ridge_regression(mtbis_train, 30, 16, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 8, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 6, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 4, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 2, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 15
print('\n')

reg = RegressionManager().ridge_regression(mtbis_train, 15, 16, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 8, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 6, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 4, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 2, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 7
print('\n')

reg = RegressionManager().ridge_regression(mtbis_train, 7, 16, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 8, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 6, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 4, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 2, alpha=alpha_1, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

points_1_20 = np.array(points)

# --------------------

points = []
alpha_2 = 0.1
print('\n Experiment 1.21: Ridge regression (\u03B1 = ' + str(alpha_2) + ') - Real MTBI = ' + str(round(real_mtbi, 4)) + '\n')

# m = 30

reg = RegressionManager().ridge_regression(mtbis_train, 30, 16, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 8, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 6, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 4, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 2, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 15
print('\n')

reg = RegressionManager().ridge_regression(mtbis_train, 15, 16, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 8, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 6, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 4, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 2, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 7
print('\n')

reg = RegressionManager().ridge_regression(mtbis_train, 7, 16, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 8, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 6, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 4, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 2, alpha=alpha_2, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

points_1_21 = np.array(points)

# ---------------

points = []
alpha_3 = 0.01
print('\n Experiment 1.22: Ridge regression (\u03B1 = ' + str(alpha_3) + ') - Real MTBI = ' + str(round(real_mtbi, 4)) + '\n')

# m = 30

reg = RegressionManager().ridge_regression(mtbis_train, 30, 16, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 8, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 6, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 4, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 30, 2, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([30, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=30, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 15
print('\n')

reg = RegressionManager().ridge_regression(mtbis_train, 15, 16, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 8, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))
coef_barplot(coefficients)

reg = RegressionManager().ridge_regression(mtbis_train, 15, 6, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 4, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 15, 2, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([15, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=15, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

# m = 7
print('\n')

reg = RegressionManager().ridge_regression(mtbis_train, 7, 16, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 16, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=16 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 8, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 8, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=8 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 6, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 6, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=6 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 4, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 4, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=4 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

reg = RegressionManager().ridge_regression(mtbis_train, 7, 2, alpha=alpha_3, output='full')
prediction = round(reg.predict(), 4)
rel_err = float(str(format(100 * np.abs(prediction - real_mtbi)/real_mtbi, '.4f')))
points.append(np.array([7, 2, rel_err]))
coefficients = [format(coef, '.4f') for coef in reg.get_coefficients()]
print('m=7, K=2 - Coefficients: ' + str(coefficients) + ' - Predicted MTBI: ' + str(prediction))

points_1_22 = np.array(points)

three_heatmaps(points_1_20, alpha_1, points_1_21, alpha_2, points_1_22, alpha_3, 'Relative error (%)')
