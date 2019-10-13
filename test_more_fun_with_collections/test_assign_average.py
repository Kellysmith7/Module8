import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(90-100, assign_average.switch_average('A'))

    def test_b(self):
        self.assertEqual(80-89, assign_average.switch_average('B'))


if __name__ == '__main__':
    unittest.main()
