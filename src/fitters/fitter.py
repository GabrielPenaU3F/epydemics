import numpy as np
from sklearn.metrics import r2_score

from src.data_io.data_manager import DataManager
from src.domain.fit import Fit
from src.domain.models.contagion_model import ContagionModel


class Fitter:

    @classmethod
    def fit(cls, country_name, dataset):
        data = DataManager.get_country_data(country_name, dataset)
        fitter = ContagionModel()
        x = np.arange(0, len(data))
        y = data[dataset].to_numpy()
        params = fitter.fit(x, y)
        explained = fitter.mean_value_function(x, *params)
        rsq = r2_score(y, explained)
        fit = Fit(country_name, dataset, x, y, explained, params, rsq)
        return fit
