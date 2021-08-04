import unittest

from src.data_manipulation.data_manager import DataManager
from src.domain.fit import Fit
from src.domain.fitter import Fitter
from src.domain.models.model import ContagionModel


class FitTest(unittest.TestCase):

    data = None

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')
        cls.data = DataManager.get_fittable_location_data('Nar Shaddaa')

    def test_partial_fit_with_out_params_must_return_tuple(self):
        fit = Fitter.fit(self.__class__.data, 'custom_data', ContagionModel(), fit_x0=(1, 0.5), output='params')
        self.assertEqual(tuple, type(fit))

    def test_partial_fit_with_out_full_must_return_fit(self):
        fit = Fitter.fit(self.__class__.data, 'custom_data', ContagionModel(), fit_x0=(1, 0.5), output='full')
        self.assertTrue(isinstance(fit, Fit))
