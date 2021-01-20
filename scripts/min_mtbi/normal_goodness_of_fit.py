import pandas
from scipy.stats import norm
from collections import Counter

from data_io.spreadsheet_data_manager import SpreadsheetDataManager
from matplotlib import pyplot as plt
import numpy as np


data_manager = SpreadsheetDataManager('../../resources/min-paises.ods', type='mtbi_min')
sheet = data_manager.get_sheet('MTBI.min')
rows_maximum_reached = sheet.filter_sheet_by_minimum_reached()

# Consider only rows with minimum x / 0.05 < x < 0.3
data = list(filter(lambda row: 0.05 <= row[2] <= 0.3, rows_maximum_reached))
# Retain only the minimums
minimums = list([data[i][2] for i in range(len(data))])

# Fit the dataset to a Normal distribution
mu, sigma = norm.fit(minimums)
x = np.linspace(np.min(minimums), np.max(minimums), 100)
print(mu)
print(sigma)

'''
plt.style.use('bmh')
plt.hist(minimums, bins=6)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.show()
'''

# Group the values in 6 bins
binned_data, bins = pandas.cut(minimums, bins=6, retbins=True, labels=False)

# Observed freqs
counter = Counter(binned_data)
of = sorted(counter.items())
print(of)

# Expected freqs
