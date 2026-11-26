import unittest
from scripts.collect_market import parse

class CollectorTests(unittest.TestCase):
    def test_missing_duplicate_and_order(self):
        self.assertEqual(parse("observation_date,DGS30\n2020-01-03,2.0\n2020-01-01,1.0\n2020-01-02,.\n2020-01-03,2.1\n2020-01-04,nan\n"), [("2020-01-01",1.0),("2020-01-03",2.1)])
    def test_legacy_header(self):
        self.assertEqual(len(parse("DATE,DGS30\n2020-01-01,1\n2020-01-02,2\n")),2)
    def test_insufficient(self):
        with self.assertRaises(ValueError):
            parse("DATE,DGS30\n2020-01-01,.\n")

if __name__ == "__main__":
    unittest.main()
