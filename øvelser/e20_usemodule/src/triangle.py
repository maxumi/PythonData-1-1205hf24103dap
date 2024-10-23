"""
My triangle module

Has:
    hypothenuse(a: float, b: float)
    area(a: float, b: float) -> float

"""


__version__ = "1.0.0.01.025.What.25"
__author__ = "My Name is Max I guess"

import math

def hypothenuse(a: float, b: float) -> float:
    """
    Calculates the length of the hypotenuse of triangle

    Args:
        a (float): Length of the first side of the triangle.
        b (float): Length of the other side of the triangle.

    Returns:
        float: The length of the hypotenuse.
    """
    return math.sqrt(a**2 + b**2)


def area(a: float, b: float) -> float:
    """
    Calculates the area of a triangle.

    Args:
        a: Length of the first side of the triangle.
        b: Length of the other side of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return 0.5 * a * b