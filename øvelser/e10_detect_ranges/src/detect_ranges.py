#!/usr/bin/env python3

def detect_ranges(L: list):
    temp_list = sorted(L)
    
    return_list = []
    i = 0
    while i < len(temp_list):
        start = temp_list[i]
        # While within range(first element to next to last) and the next value is consecutive(number equals +1 like 4+1 = 5)
        # Its done so it can check the last number
        while i < len(temp_list) - 1 and temp_list[i] + 1 == temp_list[i + 1]:
            i += 1
        end = temp_list[i]
        
        # If start equals end, make it a tuple of range
        if start == end:
            return_list.append(start)
        else:
            return_list.append((start, end + 1))
        i += 1

    return return_list

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
