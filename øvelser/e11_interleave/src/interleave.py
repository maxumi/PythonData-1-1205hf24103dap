#!/usr/bin/env python3

def interleave(*lists):
    zipped_list = list(zip(*lists))

    new_list = []

    for tupple in zipped_list:
        for element in tupple:
            new_list.append(element)



    return new_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
