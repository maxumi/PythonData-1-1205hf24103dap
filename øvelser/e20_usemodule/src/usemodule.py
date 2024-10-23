#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():

    # Calculate the hypothenuse
    hypotenuse_length = triangle.hypothenuse(3, 4)
    print(f"The length of the hypotenuse for sides {3} and {4} is: {hypotenuse_length}")

    # Calculate the area
    triangle_area = triangle.area(3, 4)
    print(f"The area of the triangle with sides {3} and {4} is: {triangle_area}")

if __name__ == "__main__":
    main()