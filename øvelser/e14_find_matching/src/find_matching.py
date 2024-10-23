#!/usr/bin/env python3

def find_matching(L, pattern):
    return_list = []
    for index, value in enumerate(L):
        # Check if the pattern exists in the current string
        if pattern in value:
            # If found, add only the index to the result list
            return_list.append(index)
    return return_list

def main():
    result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(result)
    pass

if __name__ == "__main__":
    main()
