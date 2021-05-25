import numpy as np

from src.data_manipulation.data_manager import DataManager
from src.domain.fitter import Fitter
from src.domain.models.model import ContagionModel

DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')
data = DataManager.get_raw_cumulative_data('Coruscant', end=40)
model = ContagionModel()

mtbis = []
for i in range(30, 41):
    sliced_data = data[0:i]
    x = np.arange(1, i+1, 1)
    y = sliced_data
    rho, gamma_per_rho = tuple(model.fit(x, y, x0=(0, 1)))
    s = i
    k_minus_one = data[s - 1]  # Ésto es porque los índices en Python van desde 0
    mtbi = Fitter.calculate_conditional_mtbi(s, k_minus_one, rho, gamma_per_rho, formula='approx_conditional')
    print(str(i) + ': ' + str(mtbi))
