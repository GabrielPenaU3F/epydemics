import unittest

from src.data_manipulation.argument_manager import ArgumentManager
from src.exceptions.exceptions import InvalidArgumentException
from src.repository.source_repository import SourceRepository


class ArgumentManagerTest(unittest.TestCase):

    # Source validations

    def test_owid_source_must_be_supported(self):
        self.assertTrue(ArgumentManager.validate_source('owid'))

    def test_mapache_arg_source_must_be_supported(self):
        self.assertTrue(ArgumentManager.validate_source('mapache_arg'))

    def test_custom_source_must_be_supported(self):
        self.assertTrue(ArgumentManager.validate_source('custom'))

    def test_ministerio_de_salud_source_must_not_be_supported(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_source('ministerio_de_salud')
        self.assertEqual(error.exception.strerror, 'The requested source is not supported')

    # Dataset validations

    def test_owid_source_must_support_total_cases_dataset(self):
        source = SourceRepository.retrieve_data_source('owid')
        self.assertTrue(ArgumentManager.validate_dataset(source, 'total_cases'))

    def test_owid_source_must_support_total_deaths_dataset(self):
        source = SourceRepository.retrieve_data_source('owid')
        self.assertTrue(ArgumentManager.validate_dataset(source, 'total_deaths'))

    def test_owid_source_must_not_support_casos_dataset(self):
        source = SourceRepository.retrieve_data_source('owid')
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_dataset(source, 'casos')
        self.assertEqual(error.exception.strerror, 'Requested dataset is not supported')

    def test_mapache_arg_source_must_support_nue_casosconf_diff_dataset(self):
        source = SourceRepository.retrieve_data_source('mapache_arg')
        self.assertTrue(ArgumentManager.validate_dataset(source, 'nue_casosconf_diff'))

    def test_mapache_arg_source_must_support_nue_fallecidos_diff_dataset(self):
        source = SourceRepository.retrieve_data_source('mapache_arg')
        self.assertTrue(ArgumentManager.validate_dataset(source, 'nue_fallecidos_diff'))

    def test_mapache_arg_source_must_not_support_casos_dataset(self):
        source = SourceRepository.retrieve_data_source('mapache_arg')
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_dataset(source, 'casos')
        self.assertEqual(error.exception.strerror, 'Requested dataset is not supported')

    def test_custom_source_must_support_custom_data_dataset(self):
        source = SourceRepository.retrieve_data_source('custom')
        self.assertTrue(ArgumentManager.validate_dataset(source, 'custom_data'))

    def test_custom_source_must_not_support_total_deaths_dataset(self):
        source = SourceRepository.retrieve_data_source('custom')
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_dataset(source, 'total_deaths')
        self.assertEqual(error.exception.strerror, 'Requested dataset is not supported')

    # Index validations

    def test_dataset_of_length_10_with_start_5_and_end_9_must_be_accepted(self):
        self.assertTrue(ArgumentManager.validate_indexes(10, 5, 9))

    def test_dataset_of_length_10_with_start_5_and_end_None_must_be_accepted(self):
        self.assertTrue(ArgumentManager.validate_indexes(10, 5, None))

    def test_dataset_of_length_10_with_start_5_and_end_12_must_raise_exception(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_indexes(10, 5, 12)
        self.assertEqual(error.exception.strerror, 'End argument cannot exceed dataset length')

    def test_dataset_of_length_10_with_start_12_and_end_14_must_raise_exception(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_indexes(10, 12, 14)
        self.assertEqual(error.exception.strerror, 'End argument cannot exceed dataset length')

    def test_dataset_of_length_10_with_start_12_and_end_7_must_raise_exception(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_indexes(10, 12, 7)
        self.assertEqual(error.exception.strerror, 'Start argument cannot exceed end argument')

    def test_dataset_of_length_10_with_start_5_and_end_2_must_raise_exception(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_indexes(10, 5, 2)
        self.assertEqual(error.exception.strerror, 'Start argument cannot exceed end argument')

    def test_dataset_of_length_10_with_start_12_and_end_None_must_raise_exception(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_indexes(10, 12, None)
        self.assertEqual(error.exception.strerror, 'Start argument cannot exceed dataset length')


if __name__ == '__main__':
    unittest.main()
