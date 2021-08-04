import unittest

from src.data_manipulation.data_manager import DataManager
from src.domain.fitter import Fitter


class FitModelContagionOWIDTests(unittest.TestCase):

    arg_early_fit = None
    arg_mitigation_fit = None

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset()
        cls.arg_early_fit = Fitter.fit_model(location='Argentina', dataset='total_cases', model='contagion',
                                             start=1, end=200, x0=(0.1, 1))
        cls.arg_mitigation_fit = Fitter.fit_model(location='Argentina', dataset='total_cases', model='contagion',
                                                  start=200, end=300, x0=(0.1, 1))

    def test_argentina_early_stage_rho_parameter_should_be_0_dot_130(self):
        rho = self.__class__.arg_early_fit.get_params()[0]
        self.assertAlmostEqual(0.130, rho, places=3)

    def test_argentina_early_stage_gamma_by_rho_parameter_should_be_4_dot_501(self):
        gamma_by_rho = self.__class__.arg_early_fit.get_params()[1]
        self.assertAlmostEqual(4.502, gamma_by_rho, places=3)

    def test_argentina_early_stage_rsq_should_be_0_dot_999(self):
        rsq = self.__class__.arg_early_fit.get_rsq()
        self.assertAlmostEqual(0.999, rsq, places=3)

    def test_argentina_mitigation_stage_rho_parameter_should_be_216070(self):
        rho = self.__class__.arg_mitigation_fit.get_params()[0]
        self.assertAlmostEqual(216070, rho, places=0)

    def test_argentina_mitigation_stage_gamma_by_rho_parameter_should_be_0_dot_807(self):
        gamma_by_rho = self.__class__.arg_mitigation_fit.get_params()[1]
        self.assertAlmostEqual(0.807, gamma_by_rho, places=3)

    def test_argentina_mitigation_stage_rsq_should_be_0_dot_987(self):
        rsq = self.__class__.arg_mitigation_fit.get_rsq()
        self.assertAlmostEqual(0.987, rsq, places=3)


if __name__ == '__main__':
    unittest.main()
