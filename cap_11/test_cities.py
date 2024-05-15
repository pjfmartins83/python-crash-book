import unittest
from city_functions import city_country


class CityCountryTest(unittest.TestCase):

    def test_city_country_name(self):
        result = city_country("Santiago", "Chile")
        self.assertEqual("Santiago, Chile", result)

    def test_city_country_population(self):
        result = city_country("Santiago", "Chile", 5000000)
        self.assertEqual("Santiago, Chile - population 5000000", result)


unittest.main()
