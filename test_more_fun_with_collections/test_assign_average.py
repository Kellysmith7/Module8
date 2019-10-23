import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual('Score is between 90 and 100', assign_average.switch_average('a'))


if __name__ == '__main__':
    unittest.main()
