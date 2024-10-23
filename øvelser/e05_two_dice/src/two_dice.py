#!/usr/bin/env python3


def main():
    expected = 5

    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == expected:
                print(f"({i},{j})")
        
    pass

if __name__ == "__main__":
    main()
