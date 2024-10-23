#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:  # 2 solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print((root1, root2))
        return (root1, root2)
    elif discriminant == 0:  # 1 solution
        root = -b / (2*a)
        print((root, root))
        return (root,root)
    else:  # no real solution
        print(None)
        return None


def main():
    solve_quadratic(1, -3, 2)  # Test case with two real roots
    solve_quadratic(1, 2, 1)   # Test case with one real root
    solve_quadratic(1, 0, 1)   # Test case with no real roots

if __name__ == "__main__":
    main()
