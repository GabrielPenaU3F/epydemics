from sklearn.metrics import r2_score

from src.data_io.data_manager import DataManager
from src.domain.fit import Fit
from src.domain.models.contagion_model import ContagionModel


class Fitter:

    @classmethod
    def fit(cls, country_name, dataset, start, end, x0):
        data = DataManager.get_country_data(country_name, dataset, start, end)
        model = ContagionModel()
        x = data.index.to_numpy()
        y = data[dataset].to_numpy()
        params = model.fit(x, y, x0)
        explained = model.mean_value_function(x, *params)
        rsq = r2_score(y, explained)
        fit = Fit(country_name, dataset, x, y, explained, params, rsq)
        return fit

    @classmethod
    def perform_range_fits(cls, country_name, dataset, start, end, start_from, fit_x0):
        data = DataManager.get_country_data(country_name, dataset, start, end)
        model = ContagionModel()
        parameter_list = []
        for i in range(start_from, len(data) + 1):
            sliced_data = DataManager.slice_data_by_index(data, 1, i)
            x = sliced_data.index.to_numpy()
            y = sliced_data[dataset].to_numpy()
            params = tuple(model.fit(x, y, x0=fit_x0))
            parameter_list.append(params)
        return parameter_list
