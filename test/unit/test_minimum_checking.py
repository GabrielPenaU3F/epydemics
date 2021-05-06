import unittest
import src.utils.checking_utils as checker


class MinimumCheckingTests(unittest.TestCase):

    def test_array_with_reached_minimum(self):
        array = [10, 9, 8, 7, 8, 9, 10]
        self.assertTrue(checker.check_if_minimum_was_reached(array))

    def test_array_without_reached_minimum(self):
        array = [10, 9, 8, 7, 6, 5, 4]
        self.assertFalse(checker.check_if_minimum_was_reached(array))


if __name__ == '__main__':
    unittest.main()
