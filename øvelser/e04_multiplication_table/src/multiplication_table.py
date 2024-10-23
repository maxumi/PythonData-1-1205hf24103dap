#!/usr/bin/env python3


def main():
    numb = 10
    for i in range(1, numb+1): # +1 is to say it stops at 11 but will still only go from 1-10.
        for j in range(1, numb+1):
            print(f"{i*j}\t", end="") # End is to make sure it stays on the same line
        print()  

if __name__ == "__main__":
    main()
