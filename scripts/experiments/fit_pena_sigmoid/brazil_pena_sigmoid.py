from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics

DataManager.load_dataset('owid')

# epydemics.show_cumulative_data_curve('Brazil')

fit = epydemics.fit_model('Brazil', model='pena_sigmoid', end=250,
                          x0=(0.2, 400, -1), output=True, pretrain=False)
gamma, l, M = fit.get_params()
rsq = fit.get_rsq()

print('--- Params ---')
print(f'Gamma = {gamma}')
print(f'l = {l}')
print(f'M = {M}')

print('--- Goodness of fit ---')
print(f'R2 = {rsq}')
