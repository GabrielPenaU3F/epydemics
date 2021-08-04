import numpy as np
from sklearn.metrics import r2_score

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep

from matplotlib import pyplot as plt

from src.repository.model_repository import ModelRepository

DataManager.load_dataset('owid')
pm = PlotManager.get_instance()
fig, axes = plt.subplots(1, 2)

start = 370
end = None
lugar = 'Argentina'

ax_modelo = axes[0]
fit = ep.fit_model(lugar, start=start, end=end, output=False)

x = fit.get_x_data()
real_data = fit.get_y_data()
explained = fit.get_explained_data()
params = fit.get_params()
rsq = fit.get_rsq()
ax_modelo.plot(x, real_data, linewidth=1, color='#263859', linestyle='--', label='Real data')
ax_modelo.plot(x, explained, linewidth=1, color='#ca3e47', linestyle='-',
               label='Model: \n \u03C1 = ' + str(round(params[0], 4)) +
                     '\n \u03B3 / \u03C1 = ' + str(round(params[1], 4)) +
                     '\n R2 = ' + str(round(rsq, 4))
               )
pm.config_axis_plain_style(ax_modelo)
pm.config_plot_background(ax_modelo)
ax_modelo.legend()

ax_outlier = axes[1]
model = ModelRepository.retrieve_model('contagion')
real_data_with_outlier = real_data.copy()

# for i in range(20, len(real_data)):
#    real_data_with_outlier[i] += 10**6
# real_data_with_outlier[20] = 10**6
# real_data_with_outlier[30] = 10
# real_data_with_outlier[40] = 10**7

params_out = model.fit_model(x, real_data_with_outlier, x0=(1, 0.5))
explained_outlier = model.mean_value_function(x, *params_out)
rsq_outlier = r2_score(real_data_with_outlier, explained_outlier)
ax_outlier.plot(x, real_data_with_outlier, linewidth=1, color='#263859', linestyle='--', label='Real data with outlier')
ax_outlier.plot(x, explained_outlier, linewidth=1, color='#ca3e47', linestyle='-',
                label='Model (with outlier): \n \u03C1 = ' + str(round(params_out[0], 4)) +
                      '\n \u03B3 / \u03C1 = ' + str(round(params_out[1], 4)) +
                      '\n R2 = ' + str(round(rsq_outlier, 4))
                )
pm.config_axis_plain_style(ax_outlier)
pm.config_plot_background(ax_outlier)
ax_outlier.legend()

plt.show()
