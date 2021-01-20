from src.io.spreadsheet_data_manager import SpreadsheetDataManager
from matplotlib import pyplot as plt
import numpy as np


data_manager = SpreadsheetDataManager('../../resources/min-paises.ods', type='mtbi_min')
sheet = data_manager.get_sheet('MTBI.min')
rows_maximum_reached = sheet.filter_sheet_by_minimum_reached()

# Retain only the minimums
minimums = list([rows_maximum_reached[i][2] for i in range(len(rows_maximum_reached))])

# Exploratory analysis

print("\n----------------------\n")
print("Number of values: " + str(len(minimums)))
print("Mean: %0.4f" % np.mean(minimums))
print("Median: %0.4f" % np.median(minimums))
print("Variance: %0.4f" % np.var(minimums))
print("SD: %0.4f" % np.sqrt(np.var(minimums)))
print("Minimum: %0.4f" % np.min(minimums))
print("Maximum: %0.4f" % np.max(minimums))

plt.style.use('bmh')
plt.hist(minimums, bins=int(np.sqrt(len(minimums))))
plt.show()



