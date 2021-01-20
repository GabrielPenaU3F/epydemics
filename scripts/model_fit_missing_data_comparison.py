from src.analyzers.contagion_fitter import ContagionFitter
from src.io.url_data_manager import URLDataManager
from src.plotter import Plotter
from matplotlib import pyplot as plt

url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'

manager = URLDataManager(url)

arg_data_1 = manager.get_cases_from_country('Argentina')
arg_data_2 = manager.get_cases_from_country('Argentina')

arg_data_1.locf_nans()
arg_data_2.delete_nans()

fitter = ContagionFitter()
plotter = Plotter()

x1 = arg_data_1.get_days()
y1 = arg_data_1.get_values()
x2 = arg_data_2.get_days()
y2 = arg_data_2.get_values()

a1, b1 = fitter.fit(x1, y1)
a2, b2 = fitter.fit(x2, y2)

prediction_1 = ContagionFitter().mean_value_function(x1, a1, b1)
prediction_2 = ContagionFitter().mean_value_function(x2, a2, b2)
fig, axes = plt.subplots(1, 2)
axes[0].plot(x1, y1, linewidth=1, color='#263859', linestyle='--')
axes[0].plot(x1, prediction_1, linewidth=1, color='red', linestyle='-',
             label='Carry forward fit')
axes[1].plot(x2, y2, linewidth=1, color='#263859', linestyle='--')
axes[1].plot(x2, prediction_2, linewidth=1, color='blue', linestyle='-',
             label='Delete missing data fit')

plotter.format_plot(axes[0])
plotter.format_plot(axes[1])

plt.show()


