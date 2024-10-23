#!/usr/bin/env python3

import math

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ").strip().lower() # removes whitespace and makes it lowercase

        if shape == "":
            break

        if shape == "triangle":
            base = float(input("Give the base of the triangle: ")) # Input should be able to be float
            height = float(input("Give the height of the triangle: "))
            area = 0.5 * base * height
            print(f"The area is {area}")

        elif shape == "rectangle":
            width = float(input("Give the width of the rectangle: "))
            height = float(input("Give the height of the rectangle: "))
            area = width * height
            print(f"The area is {area}")

        elif shape == "circle":
            radius = float(input("Give the radius of the circle: "))
            area = math.pi * radius ** 2
            print(f"The area is {area}")

        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
