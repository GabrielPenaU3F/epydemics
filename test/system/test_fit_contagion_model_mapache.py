import unittest

from src.data_manipulation.data_manager import DataManager
from src.fitters.fitter import Fitter


class FitContagionModelMapacheTests(unittest.TestCase):

    caba_early_fit = None
    caba_mitigation_fit = None

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset('mapache_arg')
        cls.caba_early_fit = Fitter.fit('CABA', dataset='', start=1, end=150, x0=(0.1, 1))
        cls.caba_mitigation_fit = Fitter.fit('CABA', dataset='', start=150, end=260, x0=(0.1, 1))

    def test_caba_early_stage_rho_parameter_should_be_0_dot_178(self):
        rho = self.__class__.caba_early_fit.get_params()[0]
        self.assertAlmostEqual(0.178, rho, places=3)

    def test_argentina_early_stage_gamma_by_rho_parameter_should_be_3_dot_742(self):
        gamma_by_rho = self.__class__.caba_early_fit.get_params()[1]
        self.assertAlmostEqual(3.742, gamma_by_rho, places=3)

    def test_argentina_early_stage_rsq_should_be_0_dot_998(self):
        rsq = self.__class__.caba_early_fit.get_rsq()
        self.assertAlmostEqual(0.998, rsq, places=3)

    def test_argentina_mitigation_stage_rho_parameter_should_be_21201(self):
        rho = self.__class__.caba_mitigation_fit.get_params()[0]
        self.assertAlmostEqual(21201, rho, places=0)

    def test_argentina_mitigation_stage_gamma_by_rho_parameter_should_be_0_dot_766(self):
        gamma_by_rho = self.__class__.caba_mitigation_fit.get_params()[1]
        self.assertAlmostEqual(0.766, gamma_by_rho, places=3)

    def test_argentina_mitigation_stage_rsq_should_be_0_dot_989(self):
        rsq = self.__class__.caba_mitigation_fit.get_rsq()
        self.assertAlmostEqual(0.989, rsq, places=3)

if __name__ == '__main__':
    unittest.main()
