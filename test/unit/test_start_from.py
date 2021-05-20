import unittest

from src.data_manipulation.argument_manager import ArgumentManager
from src.exceptions.exceptions import InvalidArgumentException


class StartFromArgumentTests(unittest.TestCase):

    def test_start_from_lower_than_start_should_raise_error(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ArgumentManager.determine_start_from(20, 10)
        self.assertEqual(error.exception.strerror, 'start_from argument must not exceed start argument')

    def test_start_from_must_be_30_if_start_and_start_from_are_not_specified(self):
        default_start = 1
        default_start_from = None
        start_from = ArgumentManager.determine_start_from(default_start, default_start_from)
        self.assertEqual(30, start_from)

    def test_start_from_must_be_40_if_start_is_10_and_start_from_is_not_specified(self):
        default_start_from = None
        start_from = ArgumentManager.determine_start_from(10, default_start_from)
        self.assertEqual(39, start_from)

    def test_start_from_must_be_40_if_start_is_not_specified_but_start_from_is_40(self):
        default_start = 1
        start_from = ArgumentManager.determine_start_from(default_start, 40)
        self.assertEqual(40, start_from)


if __name__ == '__main__':
    unittest.main()
