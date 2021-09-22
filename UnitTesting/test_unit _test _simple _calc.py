import unittest
from simple_calc import SimpleCalc


class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2,4),6)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(5,1),4)

