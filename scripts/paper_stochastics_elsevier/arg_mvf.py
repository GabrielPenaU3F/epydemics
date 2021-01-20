import numpy as np

import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

from src.analyzers.contagion_fitter import ContagionFitter
from src.io.url_data_manager import URLDataManager
from src.statistics.goodness_of_fit_meter import GoodnessOfFitMeter

url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'
manager = URLDataManager(url)
arg_data = manager.get_cases_from_country('Argentina')
arg_data.locf_nans()

arg_times = arg_data.get_days()
arg_ci = arg_data.get_values()

bc = ContagionFitter()

a, b = bc.fit(arg_times, arg_ci)
mean_values = bc.mean_value_function(arg_times, a, b)
coef_r2 = GoodnessOfFitMeter().calculate_coefficient_of_determination(mean_values, arg_ci)

print("rho: ", a)
print("gamma: ", b * a)
print("gamma/rho: ", b)
print("r2: ", coef_r2)

plt.style.use('bmh')
fig, axes = plt.subplots(figsize=(8, 5))

axes.set_xlabel('Time (days)')
axes.set_ylabel('Total cases')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
#axes.patch.set_edgecolor('black')
#axes.patch.set_linewidth('1')
#axes.set_facecolor("#ffffff")
#axes.grid(color='black', linestyle='--', linewidth=0.5)

axes.plot(arg_times, arg_ci, linewidth=1, color='black', linestyle='-',
          label='Real data (' + arg_data.get_country_name() + ')')
axes.plot(arg_times, mean_values, linewidth=1, color='red', linestyle='-',
          label='Proposed model')

axes.legend(prop={'size': 13})
plt.show()
