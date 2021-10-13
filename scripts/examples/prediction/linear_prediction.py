import numpy as np

from src.data_manipulation.data_manager import DataManager
from src.domain.regression_manager import RegressionManager
from src.interface import epydemics as ep

DataManager.load_dataset('owid')

# We will do a 1-day prediction of the MTBI using a linear regression model

# Step 1: obtain the MTBIS
mtbis = np.array(ep.calculate_mtbi('Argentina', start=1, end=229, unit='sec',
                 start_from=30, output=False, formula='approx_conditional'))

# Step 2: define the train set. Typically the train set will be the end of the dataset,
# which allows to predict an unknown value. However, we will perform a comparison with kown data
mtbis_train = mtbis[120:199]

# Step 3: define the regression parameters. We shall use a model of order K with m samples
m = 15
K = 8
reg = RegressionManager().linear_regression(mtbis, m, K, output='full')

# Step 4: use the model to predict and compare to the real MTBI value
print('Real MTBI: ' + str(mtbis[199]))
print('Predicted MTBI: ' + str(reg.predict()))
