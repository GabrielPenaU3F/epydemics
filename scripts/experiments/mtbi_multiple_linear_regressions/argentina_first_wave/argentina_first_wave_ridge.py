import numpy as np

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

# print('Experiment 1.2: Ridge regression (\u03B1 = 0.4) - Real MTBI = ' + str(round(mtbis[199], 4)) + '\n')
#
# # m = 30
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 16, alpha=0.4, output='full')
# print('m=30, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 8, alpha=0.4, output='full')
# print('m=30, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 6, alpha=0.4, output='full')
# print('m=30, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 4, alpha=0.4, output='full')
# print('m=30, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 2, alpha=0.4, output='full')
# print('m=30, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# # m = 15
# print('\n')
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 16, alpha=0.4, output='full')
# print('m=15, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 8, alpha=0.4, output='full')
# print('m=15, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 6, alpha=0.4, output='full')
# print('m=15, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 4, alpha=0.4, output='full')
# print('m=15, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 2, alpha=0.4, output='full')
# print('m=15, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# # m = 7
# print('\n')
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 16, alpha=0.4, output='full')
# print('m=7, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 8, alpha=0.4, output='full')
# print('m=7, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 6, alpha=0.4, output='full')
# print('m=7, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 4, alpha=0.4, output='full')
# print('m=7, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 2, alpha=0.4, output='full')
# print('m=7, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

# --------------------

# print('Experiment 1.21: Ridge regression (\u03B1 = 0.1) - Real MTBI = ' + str(round(mtbis[199], 4)) + '\n')
#
# # m = 30
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 16, alpha=0.1, output='full')
# print('m=30, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 8, alpha=0.1, output='full')
# print('m=30, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 6, alpha=0.1, output='full')
# print('m=30, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 4, alpha=0.1, output='full')
# print('m=30, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 2, alpha=0.1, output='full')
# print('m=30, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# # m = 15
# print('\n')
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 16, alpha=0.1, output='full')
# print('m=15, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 8, alpha=0.1, output='full')
# print('m=15, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 6, alpha=0.1, output='full')
# print('m=15, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 4, alpha=0.1, output='full')
# print('m=15, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 2, alpha=0.1, output='full')
# print('m=15, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# # m = 7
# print('\n')
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 16, alpha=0.1, output='full')
# print('m=7, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 8, alpha=0.1, output='full')
# print('m=7, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 6, alpha=0.1, output='full')
# print('m=7, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 4, alpha=0.1, output='full')
# print('m=7, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 2, alpha=0.1, output='full')
# print('m=7, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

# ---------------

# print('Experiment 1.22: Ridge regression (\u03B1 = 0.01) - Real MTBI = ' + str(round(mtbis[199], 4)) + '\n')
#
# # m = 30
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 16, alpha=0.01, output='full')
# print('m=30, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 8, alpha=0.01, output='full')
# print('m=30, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 6, alpha=0.01, output='full')
# print('m=30, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 4, alpha=0.01, output='full')
# print('m=30, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 30, 2, alpha=0.01, output='full')
# print('m=30, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# # m = 15
# print('\n')
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 16, alpha=0.01, output='full')
# print('m=15, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 8, alpha=0.01, output='full')
# print('m=15, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 6, alpha=0.01, output='full')
# print('m=15, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 4, alpha=0.01, output='full')
# print('m=15, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 15, 2, alpha=0.01, output='full')
# print('m=15, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# # m = 7
# print('\n')
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 16, alpha=0.01, output='full')
# print('m=7, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 8, alpha=0.01, output='full')
# print('m=7, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 6, alpha=0.01, output='full')
# print('m=7, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 4, alpha=0.01, output='full')
# print('m=7, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
#
# reg = RegressionManager().ridge_regression(mtbis, 7, 2, alpha=0.01, output='full')
# print('m=7, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

# ---------------------

print('Experiment 1.23: Ridge regression (\u03B1 = 1) - Real MTBI = ' + str(round(mtbis[199], 4)) + '\n')

# m = 30

reg = RegressionManager().ridge_regression(mtbis, 30, 16, alpha=1, output='full')
print('m=30, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 30, 8, alpha=1, output='full')
print('m=30, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 30, 6, alpha=1, output='full')
print('m=30, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 30, 4, alpha=1, output='full')
print('m=30, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 30, 2, alpha=1, output='full')
print('m=30, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

# m = 15
print('\n')

reg = RegressionManager().ridge_regression(mtbis, 15, 16, alpha=1, output='full')
print('m=15, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 15, 8, alpha=1, output='full')
print('m=15, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 15, 6, alpha=1, output='full')
print('m=15, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 15, 4, alpha=1, output='full')
print('m=15, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 15, 2, alpha=1, output='full')
print('m=15, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

# m = 7
print('\n')

reg = RegressionManager().ridge_regression(mtbis, 7, 16, alpha=1, output='full')
print('m=7, K=16 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 7, 8, alpha=1, output='full')
print('m=7, K=8 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 7, 6, alpha=1, output='full')
print('m=7, K=6 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 7, 4, alpha=1, output='full')
print('m=7, K=4 - Predicted MTBI: ' + str(round(reg.predict(), 4)))

reg = RegressionManager().ridge_regression(mtbis, 7, 2, alpha=1, output='full')
print('m=7, K=2 - Predicted MTBI: ' + str(round(reg.predict(), 4)))
