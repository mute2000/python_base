import unittest

from frame.practice.test import TestAdd

suite = unittest.TestSuite()

suite.addTest(TestAdd('test_add'))

runner = unittest.TextTestRunner()

runner.run(suite)