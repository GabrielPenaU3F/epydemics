import pandas
from scipy.stats import expon
from collections import Counter

from src.io.spreadsheet_data_manager import SpreadsheetDataManager
from matplotlib import pyplot as plt
import numpy as np


data_manager = SpreadsheetDataManager('../../resources/min-paises.ods', type='mtbi_min')
sheet = data_manager.get_sheet('MTBI.min')
rows_maximum_reached = sheet.filter_sheet_by_minimum_reached()

minimums = list([rows_maximum_reached[i][2] for i in range(len(rows_maximum_reached))])

# Fit the dataset to a Exp distribution
lambda_ = 1/np.mean(minimums)
x = np.linspace(np.min(minimums), np.max(minimums), 100)
print(lambda_)

plt.style.use('bmh')
plt.hist(minimums, bins=6)
plt.plot(x, expon.pdf(x, loc=0, scale=(1/lambda_)))
plt.show()

'''
# Group the values in 6 bins
binned_data, bins = pandas.cut(minimums, bins=6, retbins=True, labels=False)

# Observed freqs
counter = Counter(binned_data)
of = sorted(counter.items())
print(of)

# Expected freqs
'''