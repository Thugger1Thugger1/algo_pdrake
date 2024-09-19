from gcd import gcd

class Fraction:
    def __init__(self, n: int, d: int):
        self.n = n // gcd(n, d)
        self.d = d // gcd(n, d)

    def __str__(self):
        return f'{self.n}/{self.d}'
        
    def __repr__(self):
        return(str(self))
        
    def __add__(self, other):
        return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)

    def __sub__(self, other):
        return Fraction(self.n * other.d - other.n * self.d, self.d * other.d)
   
    def __mul__(self, other):
        return Fraction(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):
        return self * Fraction(other.d, other.n)

    def __float__(self):
        return self.n/self.d
    