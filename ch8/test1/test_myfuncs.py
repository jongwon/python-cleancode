import unittest
from ch8.test1.myfuncs import add_one, abs


class TestMyFuncs(unittest.TestCase):
    """
    1+1=2
    """
    def test_1_더하기_1_은_2(self):
        self.assertEqual(add_one(1), 2)


class TestAbs(unittest.TestCase):
    """
    |1|=1
    |-3|=3
    """

    def test_abs_positive(self):
        self.assertEqual(abs(1), 1)

    def test_abs_음수(self):
        self.assertEqual(abs(-3), 3)

    def test_0_의_절대값은_0(self):
        self.assertEqual(abs(0), 0)