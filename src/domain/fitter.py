import numpy as np
from sklearn.metrics import r2_score

from src.data_manipulation.data_manager import DataManager
from src.data_manipulation.dataframe_slicer import DataframeSlicer
from src.domain.fit import Fit
from src.domain.models.model import ContagionModel
from src.domain.unit_converter import DaysConverter
from src.exceptions.exceptions import InvalidArgumentException
from src.repository.model_repository import ModelRepository


class Fitter:

    residual_types = ['true', 'abs', 'square']

    @classmethod
    def fit_model(cls, location, dataset, model, start, end, x0):
        data = DataManager.get_fittable_location_data(location, dataset, start, end)
        dataset = DataManager.choose_dataset(dataset)
        model = ModelRepository.retrieve_model(model)
        fit = cls.fit(data, dataset, model, x0)
        return fit

    @classmethod
    def fit_parameters_over_time(cls, location, dataset, start, end, start_from, fit_x0, output='params'):
        dataset = DataManager.choose_dataset(dataset)
        data = DataManager.get_fittable_location_data(location, dataset, start, end)
        new_end = len(data) + 1
        model = ContagionModel()
        output_list = []
        for i in range(start_from, new_end):
            sliced_data = DataframeSlicer.slice_rows_by_index(data, 1, i)
            output_list.append(cls.fit(sliced_data, dataset, model, fit_x0, output))
        return output_list

    @classmethod
    def fit(cls, data, dataset, model, fit_x0, output='full'):
        x = data.index.values
        y = data[dataset].values
        params = model.fit(x, y, fit_x0)
        out = tuple(params)
        if output == 'full':
            explained = model.mean_value_function(x, *params)
            rsq = r2_score(y, explained)
            out = Fit(x, y, explained, params, rsq)
        return out

    @classmethod
    def calculate_mtbis(cls, location, dataset, start, end, start_from, unit, fit_x0, formula):
        dataset = DataManager.choose_dataset(dataset)
        data = DataManager.get_fittable_location_data(location, dataset, start, end)
        new_end = len(data) + 1
        model = ContagionModel()
        mtbis = []
        for i in range(start_from, new_end):
            sliced_data = DataframeSlicer.slice_rows_by_index(data, 1, i)
            params = cls.fit(sliced_data, dataset, model, fit_x0, output='params')
            rho = params[0]
            gamma_per_rho = params[1]
            s = i
            k_minus_one = DataManager.get_single_datum(location, s, dataset, start)
            mtbi = cls.calculate_conditional_mtbi(s, k_minus_one, rho, gamma_per_rho, formula)
            mtbis.append(mtbi)
        mtbis = DaysConverter.get_instance().convert_days_to(unit, mtbis)
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
        fit = cls.fit_model(location, dataset, model, start, end, fit_x0)
        y = fit.get_y_data()
        mean_values = fit.get_explained_data()
        residuals = cls.choose_residuals(y, mean_values, residual_type)
        return residuals

    @classmethod
    def compute_last_residuals_over_time(cls, location, dataset, start, end, start_from, fit_x0, residual_type):
        cls.validate_residual_type(residual_type)
        dataset = DataManager.choose_dataset(dataset)
        data = DataManager.get_fittable_location_data(location, dataset, start, end)
        new_end = len(data) + 1
        model = ContagionModel()
        mean_values = []
        for i in range(start_from, new_end):
            sliced_data = DataframeSlicer.slice_rows_by_index(data, 1, i)
            params = cls.fit(sliced_data, dataset, model, fit_x0, output='params')
            last_mean = model.mean_value_function(i, *params)
            mean_values.append(last_mean)
        y = data[dataset].values[start_from - 1:new_end]
        residuals = cls.choose_residuals(y, np.array(mean_values), residual_type)
        return residuals

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
