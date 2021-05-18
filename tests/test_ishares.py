import os
import unittest
from unittest import TestCase
import ishares

class Test(TestCase):

    def test_read_csv(self):
        d = ishares.read_csv('ICLN_holdings.csv')
        self.assertEqual(d.shape, (38, 4))

    def test_download(self):
        url = "https://www.ishares.com/us/products/239726/"
        suburl, filename = ishares.find_download(url)
        self.assertIsNotNone(suburl)
        self.assertIsNotNone(filename)

        tmp_dir = "etf_data"
        ishares.get_file(url, tmp_dir=tmp_dir)
        self.assertTrue(os.path.exists(os.path.join(tmp_dir, filename)))


    def test_sp500(self):
        url = "https://www.ishares.com/us/products/239726/"
        d = ishares.getFromURL(url)
        self.assertGreater(d.shape[0], 450)

        isins = ["US0378331005", "US5949181045"]
        self.assertTrue(all(x in d["ISIN"].values for x in isins))




if __name__ == "__main__":
    unittest.main()