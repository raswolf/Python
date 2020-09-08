import unittest
from module3.main.camper_age_input import convert_to_months


class FunctionTestCase(unittest.TestCase):
    """Tests operation with user input 5 years"""
    def test_five_years(self):
        self.assertEqual(convert_to_months(5), 60)


if __name__ == '__main__':
    unittest.main()
