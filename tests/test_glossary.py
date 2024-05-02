import unittest
from procurement_tools import Glossary


class TestGlossary(unittest.TestCase):

    def test_lookup_by_term(self):
        result = Glossary.lookup_by_term("VOSB")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["term"], "VOSB")

        # don't worry about case
        result = Glossary.lookup_by_term("vosb")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["term"], "VOSB")

    def test_lookup_by_term_fuzzy(self):
        # Assuming implementation of fuzzy search is corrected
        # Currently, it seems to be incorrect in your implementation
        result = Glossary.lookup_by_term_fuzzy("veteran-owned")
        self.assertTrue(len(result) > 0)

    def test_find_terms_valid(self):
        result = Glossary.find_terms("VOSB")
        self.assertIsNotNone(result)

    def test_get_acronyms(self):
        result = Glossary.get_acronyms()
        self.assertGreater(len(result), 1)
        self.assertIn("VOSB", result)

    def test_find_terms_invalid(self):
        term = "nonexistent"
        result = Glossary.find_terms(term)
        self.assertListEqual([], result)


# Run the tests
if __name__ == "__main__":
    unittest.main()
