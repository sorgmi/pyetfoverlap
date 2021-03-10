import os, sys
os.chdir(os.path.join(os.getcwd(), "tests"))

import unittest
loader = unittest.TestLoader()
tests = loader.discover('tests')
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)
