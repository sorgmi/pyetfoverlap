import unittest
from unittest import TestCase
import ishares

class Test(TestCase):

    def test_read_csv(self):
        d = ishares.read_csv('ICLN_holdings.csv')
        self.assertEqual(d.shape, (38, 4))




if __name__ == "__main__":
    unittest.main()