import matplotlib
from matplotlib import pyplot as plt

from statistics.goodness_of_fit_meter import calculate_coefficient_of_determination

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

from src.analyzers.contagion_fitter import ContagionFitter
from src.io.url_data_manager import URLDataManager

url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'
manager = URLDataManager(url)
uruguay_data = manager.get_cases_from_country('Uruguay')
uruguay_data.locf_nans()

uruguay_times = uruguay_data.get_days()[0:70]
uruguay_ci = uruguay_data.get_values()[0:70]

bc = ContagionFitter()

a, b = bc.fit(uruguay_times, uruguay_ci)
mean_values = bc.mean_value_function(uruguay_times, a, b)
coef_r2 = calculate_coefficient_of_determination(mean_values, uruguay_ci)

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

axes.plot(uruguay_times, uruguay_ci, linewidth=1, color='black', linestyle='-',
          label='Real data (' + uruguay_data.get_country_name() + ')')
axes.plot(uruguay_times, mean_values, linewidth=1, color='red', linestyle='-',
          label='Proposed model')

axes.legend(prop={'size': 13})
plt.show()
