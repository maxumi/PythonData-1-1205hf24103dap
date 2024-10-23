#!/usr/bin/env python3

def transform(s1: str, s2: str):
    s1s = list(map(int, s1.split()))
    s2s = list(map(int, s2.split()))
    result = [(a*b) for a,b in zip(s1s,s2s)]
    
    
    return result

def main():
    print(transform("1 5 3", "2 6 -1"))
    pass

if __name__ == "__main__":
    main()
