from matplotlib import pyplot as plt

from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics

DataManager.load_dataset('owid')

# epydemics.show_cumulative_data_curve('Argentina')
# epydemics.show_cumulative_data_curve('Brazil')

fit_ps = epydemics.fit_model('Brazil', model='pena_sigmoid', end=250,
                             x0=(0.2, 400, -1), output=False)
fit_dss = epydemics.fit_model('Brazil', model='delayed_s_shaped', end=250,
                              x0=(10, 0.01), output=False)

# fit_ps = epydemics.fit_model('Argentina', model='pena_sigmoid', end=300,
#                              x0=(0.2, 400, -1), output=False)
# fit_dss = epydemics.fit_model('Argentina', model='delayed_s_shaped', end=300,
#                               x0=(10**12, 0.0001), output=False)

gamma_ps, l_ps, M_ps = fit_ps.get_params()
a_dss, b_dss = fit_dss.get_params()
rsq_ps = fit_ps.get_rsq()
rsq_dss = fit_dss.get_rsq()

print('--- Pena Sigmoid ---')
print(f'Gamma = {gamma_ps}')
print(f'l = {l_ps}')
print(f'M = {M_ps}')
print(f'R2 = {rsq_ps}')

print('--- Delayed S-Shaped ---')
print(f'a = {a_dss}')
print(f'b = {b_dss}')
print(f'R2 = {rsq_dss}')

x = fit_ps.get_x_data()
y = fit_ps.get_y_data()
y_psig = fit_ps.get_explained_data()
y_dss = fit_dss.get_explained_data()

plt.plot(x, y, label='Real data', linestyle='--')
plt.plot(x, y_psig, label='Pena Sigmoid')
plt.plot(x, y_dss, label='Delayed S-Shaped')
plt.legend()
plt.show()
