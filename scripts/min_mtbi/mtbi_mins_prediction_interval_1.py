from src.io.spreadsheet_data_manager import SpreadsheetDataManager
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats


data_manager = SpreadsheetDataManager('../../resources/min-paises.ods', type='mtbi_min')
sheet = data_manager.get_sheet('MTBI.min')
rows_maximum_reached = sheet.filter_sheet_by_minimum_reached()

# Consider only rows with condition
data = list(filter(lambda row: 0.1 <= row[2] <= 1.5, rows_maximum_reached))
# Retain only the minimums
minimums = list([data[i][2] for i in range(len(data))])

alpha = 0.05
xbar = np.mean(minimums)
s = np.sqrt(np.var(minimums))
n = len(minimums)
df = n - 1
t = stats.t.isf(alpha/2, df=df)  # Limit of the interval (t, +inf) for which the area under the pdf is alpha/2

upper_limit = xbar + t * s * np.sqrt(1 + 1/n)
lower_limit = xbar - t * s * np.sqrt(1 + 1/n)

# Estimation and prediction interval

print("\n----------------------\n")
print("Number of values: " + str(len(minimums)))
print("Estimate: %0.4f" % np.mean(minimums))
print("Prediction interval: %0.4f < x < %0.4f at %d%%" % (lower_limit, upper_limit, (1 - alpha)*100))
