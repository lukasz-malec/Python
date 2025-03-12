from math import hypot, atan, sin, cos, sqrt

class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

    def __abs__(self):
        return hypot(self.r,self.i)

    def __repr__(self):
        return f"Zespolona({self.r}, {self.i})"

    def __str__(self):
        if self.i > 0:
            return f"({self.r}+{self.i}j)"
        elif self.i < 0:
            return f"({self.r}{self.i}j)"
        return f"({self.r} + {self.i}j)"

    def __add__(self, other):
        if isinstance(other, Zespolona):
            return Zespolona(self.r + other.r, self.i + other.i)
        elif isinstance(other, (int, float)):
            return Zespolona(self.r + other, self.i)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Zespolona):
            return Zespolona(self.r - other.r, self.i - other.i)
        elif isinstance(other, (int, float)):
            return Zespolona(self.r - other, self.i)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Zespolona):
            return Zespolona(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)
        elif isinstance(other, (int, float)):
            return Zespolona(self.r * other, self.i * other)
        return NotImplemented 
    
    def __radd__(self, other):
        return self + other 

    def __rsub__(self, other):
        return Zespolona(other, 0) - self 

    def __rmul__(self, other):
        return self * other  

    def __eq__(self, other):
        if isinstance(other, Zespolona):
            return self.i == other.i  and self.r == other.r
        return self.r == other and self.i == 0

    def __ne__(self, other):
        if isinstance(other, Zespolona):
            return self.i != other.i or  self.r != other.r
        return self.r == other or self.i == 0

    def __pow__(self, other):
        wynik = self
        for x in range(other - 1):
            wynik *= self
        return wynik


    def __truediv__(self, other):
        if isinstance(other, Zespolona):
            mianownik = other.r ** 2 + other.i ** 2
            return Zespolona((self.r * other.r + self.i * other.i) / mianownik, (self.i * other.r - self.r * other.i )/ mianownik )
        elif isinstance(other, (int, float)):
            return Zespolona(self.r / other, self.i / other )


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a ==  b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)
    print(a / b)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)
# (-1.3+1.1j)