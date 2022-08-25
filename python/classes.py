import math
import unittest

class Complex(complex):
    def __add__(self, no):
        return Complex(complex.__add__(self,no))
    def __sub__(self, no):
        return Complex(complex.__sub__(self,no))
    def __mul__(self, no):
        return Complex(complex.__mul__(self,no))
    def __truediv__(self, no):
        return Complex(complex.__truediv__(self,no))
    def mod(self):
        return Complex(complex.__abs__(self))
    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result
            
        # return '{0.real:.2f}{0.imag:+.2f}i'.format(self)

class TestComplex(unittest.TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        with open('testCases', 'r') as file:
            lines = file.readlines()
            c = map(float, lines[0].split())
            d = map(float, lines[1].split())
            self.x = Complex(*c)
            self.y = Complex(*d)

    def test_add(self):
        self.assertEqual('0.00+0.00i', str(self.x+self.y))
    def test_sub(self):
        self.assertEqual('22.00+38.00i', str(self.x-self.y))
    def test_mul(self):
       self.assertEqual('240.00-418.00i', str(self.x*self.y))
    def test_truediv(self):
        self.assertEqual('-1.00+0.00i', str(self.x/self.y))
    def test_mod_x(self):
        self.assertEqual('21.95+0.00i', str(self.x.mod()))
    def test_mod_y(self):
        self.assertEqual('21.95+0.00i', str(self.y.mod()))

    

if __name__ == '__main__':
    unittest.main()
    #print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')