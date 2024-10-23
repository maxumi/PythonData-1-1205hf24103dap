#!/usr/bin/env python3

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator MUST NOT BE ZERO")
        self.num = numerator
        self.denom = denominator

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __mul__(self, other):
        # formula: a/b * c/d = (a * c) as numerator and (b * d) as denominator
        return Rational(self.num * other.num, self.denom * other.denom)

    def __truediv__(self, other):
        # formula: a/b ÷ c/d = (a * d) as numerator and (b * c) as denominator
        return Rational(self.num * other.denom, self.denom * other.num)

    def __add__(self, other):
        # formula: a/b + c/d = (a*d + c*b) as numerator and (b*d) as denominator
        return Rational(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        # formula: a/b - c/d = (a*d - c*b) as numerator and (b*d) as denominator
        return Rational(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    def __eq__(self, other):
        # This means 10/5 == 100/50 is true
        return self.num * other.denom == other.num * self.denom

    def __gt__(self, other):
        return self.num * other.denom > other.num * self.denom

    def __lt__(self, other):
        return self.num * other.denom < other.num * self.denom




def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)  
    print(r1 / r2)  
    print(r1 + r2)  
    print(r1 - r2)  
    print(Rational(1, 2) == Rational(2, 4))  
    print(Rational(1, 2) > Rational(2, 4))   
    print(Rational(1, 2) < Rational(2, 4))   


if __name__ == "__main__":
    main()
