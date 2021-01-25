from sklearn.metrics import r2_score

from src.data_io.data_manager import DataManager
from src.domain.fit import Fit
from src.domain.models.contagion_model import ContagionModel


class Fitter:

    @classmethod
    def fit(cls, country_name, dataset, start, end):
        data = DataManager.get_country_data(country_name, dataset, start, end)
        fitter = ContagionModel()
        x = data.index.to_numpy()
        y = data[dataset].to_numpy()
        params = fitter.fit(x, y)
        explained = fitter.mean_value_function(x, *params)
        rsq = r2_score(y, explained)
        fit = Fit(country_name, dataset, x, y, explained, params, rsq)
        return fit
