import unittest

from src.data_manipulation.argument_manager import ArgumentManager
from src.exceptions.exceptions import InvalidArgumentException


class ArgumentManagerTest(unittest.TestCase):

    def test_owid_source_must_be_supported(self):
        self.assertEqual(ArgumentManager.validate_source('owid'), True)

    def test_mapache_arg_source_must_be_supported(self):
        self.assertEqual(ArgumentManager.validate_source('mapache_arg'), True)

    def test_custom_source_must_be_supported(self):
        self.assertEqual(ArgumentManager.validate_source('custom'), True)

    def test_ministerio_de_salud_source_must_not_be_supported(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.validate_source('ministerio_de_salud')
        self.assertEqual(error.exception.strerror, 'The requested source is not supported')


if __name__ == '__main__':
    unittest.main()
