#!/usr/bin/env python3

def reverse_dictionary(d: dict):
    rev_dict = {}

    for key, value in d.items():
        if isinstance(value, list):  # Check if values is a list
            for v in value:
                if v not in rev_dict: # needed or else it would clear it
                    rev_dict[v] = [] # if first time encounted then make a empty place for it so it appends later.
                rev_dict[v].append(key) 
        else: 
            if value not in rev_dict:
                rev_dict[value] = []
            rev_dict[value].append(key)
    
    return rev_dict

def main():
    original_dict = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}

    print("Original dictionary:", original_dict)
    
    reversed_dict = reverse_dictionary(original_dict)
    
    print("Reversed dictionary:", reversed_dict)

if __name__ == "__main__":
    main()
