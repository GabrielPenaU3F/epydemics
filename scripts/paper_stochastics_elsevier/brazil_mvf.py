import matplotlib
from matplotlib import pyplot as plt

from statistics.goodness_of_fit_meter import calculate_coefficient_of_determination

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

from src.analyzers.contagion_fitter import ContagionFitter
from src.io.url_data_manager import URLDataManager

url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'
manager = URLDataManager(url)
brazil_data = manager.get_cases_from_country('Brazil')
brazil_data.locf_nans()

brazil_times = brazil_data.get_days()
brazil_ci = brazil_data.get_values()

bc = ContagionFitter()

a, b = bc.fit(brazil_times, brazil_ci)
mean_values = bc.mean_value_function(brazil_times, a, b)
coef_r2 = calculate_coefficient_of_determination(mean_values, brazil_ci)

print("rho: ", a)
print("gamma: ", b * a)
print("gamma/rho: ", b)
print("r2: ", coef_r2)

plt.style.use('bmh')
fig, axes = plt.subplots(figsize=(8, 5))

axes.set_xlabel('Time (days)')
axes.set_ylabel('Total cases')
axes.ticklabel_format(axis='y', style='plain')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
#axes.patch.set_edgecolor('black')
#axes.patch.set_linewidth('1')
#axes.set_facecolor("#ffffff")
#axes.grid(color='black', linestyle='--', linewidth=0.5)

axes.plot(brazil_times, brazil_ci, linewidth=1, color='black', linestyle='-',
          label='Real data (' + brazil_data.get_country_name() + ')')
axes.plot(brazil_times, mean_values, linewidth=1, color='red', linestyle='-',
          label='Proposed model')

axes.legend(prop={'size': 13})
plt.show()
