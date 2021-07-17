import numpy as np
from sklearn.metrics import r2_score

from src.data_manipulation.data_manager import DataManager
from src.data_manipulation.dataframe_slicer import DataframeSlicer
from src.domain.fit import Fit
from src.domain.models.model import ContagionModel
from src.exceptions.exceptions import InvalidArgumentException
from src.repository.model_repository import ModelRepository


class Fitter:

    residual_types = ['true', 'abs', 'square']

    @classmethod
    def fit(cls, location, dataset, model, start, end, x0):
        source = DataManager.get_data_source()
        data = DataManager.get_fittable_location_data(location, dataset, start, end)
        dataset = DataManager.choose_dataset(dataset)
        model = ModelRepository.retrieve_model(model)
        x = data.index.values
        y = data[dataset].values
        params = model.fit(x, y, x0)
        explained = model.mean_value_function(x, *params)
        rsq = r2_score(y, explained)
        fit = Fit(source, location, dataset, x, y, explained, params, rsq)
        return fit

    @classmethod
    def fit_parameters_over_time(cls, location, dataset, start, end, start_from, fit_x0):
        dataset = DataManager.choose_dataset(dataset)
        data = DataManager.get_fittable_location_data(location, dataset, start, end)
        new_end = len(data) + 1
        model = ContagionModel()
        parameter_list = []
        for i in range(start_from, new_end):
            parameter_list.append(cls.partial_fit(data, dataset, fit_x0, 1, i, model))
        return parameter_list

    @classmethod
    def partial_fit(cls, data, dataset, fit_x0, fit_start, fit_end, model):
        sliced_data = DataframeSlicer.slice_rows_by_index(data, fit_start, fit_end)
        x = sliced_data.index.values
        y = sliced_data[dataset].values
        params = tuple(model.fit(x, y, x0=fit_x0))
        return params

    @classmethod
    def calculate_mtbis(cls, location, dataset, start, end, start_from, fit_x0, formula):
        dataset = DataManager.choose_dataset(dataset)
        data = DataManager.get_fittable_location_data(location, dataset, start, end)
        new_end = len(data) + 1
        model = ContagionModel()
        mtbis = []
        for i in range(start_from, new_end):
            params = cls.partial_fit(data, dataset, fit_x0, 1, i, model)
            rho = params[0]
            gamma_per_rho = params[1]
            s = i
            k_minus_one = DataManager.get_single_datum(location, s, dataset)
            mtbi = cls.calculate_conditional_mtbi(s, k_minus_one, rho, gamma_per_rho, formula)
            mtbis.append(mtbi)
        return mtbis

    @classmethod
    def calculate_conditional_mtbi(cls, s, k_minus_one, rho, gamma_per_rho, formula):
        if formula == 'exact_conditional':
            gamma = gamma_per_rho * rho
            return (1 + rho * s) / (gamma * k_minus_one)
        elif formula == 'approx_conditional':
            return (1 + rho * s) / (rho * ((1 + rho * s) ** gamma_per_rho - 1))

    @classmethod
    def compute_fit_residuals(cls, location, dataset, model, start, end, fit_x0, residual_type):
        cls.validate_residual_type(residual_type)
        fit = cls.fit(location, dataset, model, start, end, fit_x0)
        y = fit.get_y_data()
        mean_values = fit.get_explained_data()
        residuals = cls.choose_residuals(y, mean_values, residual_type)
        return residuals

    '''
    @classmethod
    def compute_fit_residuals(cls, location, dataset, start, end, start_from, fit_x0):
        dataset = DataManager.choose_dataset(dataset)
        data = DataManager.get_fittable_location_data(location, dataset, start, end)
        new_end = len(data) + 1
        model = ContagionModel()
        mean_values = []
        for i in range(start_from, new_end):
            params = cls.partial_fit(data, dataset, fit_x0, 1, i, model)
            x = np.arange(1, new_end)
            mean = model.mean_value_function(x, *params)
            mean_values.append(mean)
        residuals = np.array(mean_values) - data[dataset].values
        return residuals
    '''

    @classmethod
    def choose_residuals(cls, r, mean_values, residual_type):
        integer_mean_values = np.rint(mean_values)
        if residual_type == 'true':
            return integer_mean_values - r
        elif residual_type == 'abs':
            return np.abs(integer_mean_values - r)
        elif residual_type == 'square':
            return (integer_mean_values - r) ** 2

    @classmethod
    def validate_residual_type(cls, residual_type):
        if residual_type not in cls.residual_types:
            raise InvalidArgumentException('The residual type is invalid')
