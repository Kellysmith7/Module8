import unittest
from more_fun_with_collections import date_time
from datetime import date


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual((2019, 12, 5), date_time.half_birthday(date(1981, 6, 5)))


if __name__ == '__main__':
    unittest.main()
