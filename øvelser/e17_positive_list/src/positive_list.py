#!/usr/bin/env python3

def positive_list(L):
    return list(filter(lambda i: i > 0, L)) # Lambda is inline function

def main():
    print(positive_list([2,-2,0,1,-7]))
    pass

if __name__ == "__main__":
    main()
