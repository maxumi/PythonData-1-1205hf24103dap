#!/usr/bin/env python3

def main():
    list_pair = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 5]
    for p in list_pair:
        print(p)
    pass

if __name__ == "__main__":
    main()
