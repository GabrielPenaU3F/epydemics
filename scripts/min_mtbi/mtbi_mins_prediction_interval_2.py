from src.io.spreadsheet_data_manager import SpreadsheetDataManager
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats


data_manager = SpreadsheetDataManager('../../resources/min-paises.ods', type='mtbi_min')
sheet = data_manager.get_sheet('MTBI.min')
rows_maximum_reached = sheet.filter_sheet_by_minimum_reached()

# Consider only rows with condition
data = list(filter(lambda row: 0.1 <= row[2] <= 0.2, rows_maximum_reached))
# Retain only the minimums
minimums = list([data[i][2] for i in range(len(data))])

xbar = np.mean(minimums)
s = np.sqrt(np.var(minimums))
n = len(minimums)
df = n - 1

upper_limit = 0.15
t = (upper_limit - xbar) / (s * np.sqrt(1 + 1/n))
alpha = stats.t.sf(t, df=df)
# formula: x_upper = xbar + t * s * np.sqrt(1 + 1/n)

# Estimation and prediction interval

print("\n----------------------\n")
print("Number of values: " + str(len(minimums)))
print("Estimate: %0.4f" % np.mean(minimums))
print("Probability of falling under L=%0.2f: %d%%" %(upper_limit, (1-alpha) * 100))
