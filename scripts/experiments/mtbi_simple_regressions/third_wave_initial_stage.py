import numpy as np
from numpy.polynomial import polynomial as poly
from matplotlib import pyplot as plt
from scipy import optimize as opt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import r2_score

from scripts.experiments.mtbi_simple_regressions.regression_functions import exponential_function, poly_function
from scripts.experiments.useful_functions import config_regular_plot_structure
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep


DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 10
start = 351
end = 412

segment_start = 25
segment_end = 52

mtbis = np.array(ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                 start_from=start_from, output=False, formula='approx_conditional'))[segment_start:segment_end]
x_start = start_from + segment_start
t = np.arange(x_start, x_start + len(mtbis))

# Linear
t_res = t.reshape((-1, 1))
lreg = LinearRegression().fit(t_res, mtbis)
explained_linear = lreg.predict(t_res)
rsq_linear = lreg.score(t_res, mtbis)

# Polynomial
deg = 4
x0 = np.ones(deg + 1)
params, cov = opt.curve_fit(poly_function, t, mtbis, method='lm', p0=x0)
explained_poly = poly_function(t, *params)
rsq_poly = r2_score(mtbis, explained_poly)

# Exponential
params, cov = opt.curve_fit(exponential_function, t, mtbis, method='lm', p0=(1, 0.001, 0))
explained_exp = exponential_function(t, *params)
rsq_exp = r2_score(mtbis, explained_exp)

fig, axes = plt.subplots(figsize=(12, 8))
axes.plot(t, mtbis, linewidth=2, color='black', linestyle='-.', label='Real MTBI')
axes.plot(t, explained_linear, linewidth=2, color='#0008AC', linestyle='-', label='Linear')
axes.plot(t, explained_poly, linewidth=2, color='purple', linestyle='-', label=str('Polynomal deg  ' + str(deg)))
axes.plot(t, explained_exp, linewidth=2, color='green', linestyle='-', label='Exponential')
axes.ticklabel_format(axis='y', style='sci')
axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
axes.set_ylabel('MTBI (sec)', fontsize=32, labelpad=15)
config_regular_plot_structure(axes, legend_loc='upper right')
fig.tight_layout()

print('R2 scores: ')
print('Linear: ' + str(round(rsq_linear, 4)))
print('Polynomial: ' + str(round(rsq_poly, 4)))
print('Exponential: ' + str(round(rsq_exp, 4)))

plt.show()
