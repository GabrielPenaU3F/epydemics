import math

import numpy as np
from matplotlib import pyplot as plt

from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# start = 1
# end = 280
# start = 280
# end = 360
start = 370

DataManager.load_dataset('owid')
mtbis = np.array(epydemics.calculate_mtbi('Argentina', start=start, formula='approx_conditional',
                                          unit='day', output=False))
end = start + len(mtbis) + 30

mtbi_inversos = np.power(mtbis, -1)
t = np.arange(370, end)

real_data = DataManager.get_fittable_location_data('Argentina', start=400, end=end)['total_cases'].values
incidence_data = ([0] + np.diff(real_data))

plt.plot(t, mtbi_inversos)
plt.plot(t, incidence_data)

plt.show()
