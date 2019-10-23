import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual('Score is between 90 and 100', assign_average.switch_average('a'))

    def test_b(self):
        self.assertEqual('Score is between 80 and 89', assign_average.switch_average('b'))

    def test_c(self):
        self.assertEqual('Score is between 70 and 79', assign_average.switch_average('c'))

    def test_d(self):
        self.assertEqual('Score is between 60 and 69', assign_average.switch_average('d'))

    def test_f(self):
        self.assertEqual('Score is between 0 and 59', assign_average.switch_average('f'))

    def test_e(self):
        self.assertEqual("Invalid letter grade", assign_average.switch_average('e'))

    def test_1(self):
        self.assertEqual("Invalid letter grade", assign_average.switch_average('1'))



if __name__ == '__main__':
    unittest.main()
