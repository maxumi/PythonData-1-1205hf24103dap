#!/usr/bin/env python3

def triple(num):
    return num *3

def square(num):
    return num **2 # Powers of two


def main():
    for i in range(1,11):
        trip = triple(i)
        squa = square(i)
        if squa > trip:
            break
        print(f"triple({i})=={trip} square({i})=={squa}")
    pass

if __name__ == "__main__":
    main()
