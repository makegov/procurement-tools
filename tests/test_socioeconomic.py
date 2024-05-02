import unittest
from procurement_tools import Socioeconomic


class TestSocioeconomic(unittest.TestCase):

    def test_get_business_types_from_categories(self):
        categories_list = ["HUBZone", "SB"]
        expected = ["05", "1B", "XX", "JX"]
        result = Socioeconomic.get_business_types_from_categories(categories_list)
        assert result == expected


    def test_get_categories_from_business_types(self):
        business_type_list = ["2X", "8W", "A2"]
        expected = ["WOSB"]
        result = Socioeconomic.get_categories_from_business_types(business_type_list)
        assert result == expected


    def test_get_category_for_business_type(self):
        business_type = "8D"
        expected = "WOSB"
        result = Socioeconomic.get_category_for_business_type(business_type)
        assert result == expected



# Run the tests
if __name__ == "__main__":
    unittest.main()
