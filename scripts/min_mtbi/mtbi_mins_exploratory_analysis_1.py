from src.io.spreadsheet_data_manager import SpreadsheetDataManager
from matplotlib import pyplot as plt
import numpy as np


data_manager = SpreadsheetDataManager('../../resources/min-paises.ods', type='mtbi_min')
sheet = data_manager.get_sheet('MTBI.min')
rows_maximum_reached = sheet.filter_sheet_by_minimum_reached()

# Consider only rows with condition
data = list(filter(lambda row: 0.1 <= row[2] <= 1.5, rows_maximum_reached))
# Retain only the minimums
minimums = list([data[i][2] for i in range(len(data))])

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
plt.hist(minimums, bins=6)
plt.show()



