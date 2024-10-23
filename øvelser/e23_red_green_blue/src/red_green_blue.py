#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    rtn_list = []
    rgx_pattern = re.compile(
        r"""
        (\d+)        # Captures one or more digits (Red value in RGB)
        \s+          # Matches one or more whitespace characters (space, tab, etc.)
        (\d+)        # Captures one or more digits (Green value in RGB)
        \s+          # Matches one or more whitespace characters separating fields
        (\d+)        # Captures one or more digits (Blue value in RGB)
        \s+          # Matches one or more whitespace characters separating fields
        (.+)         # Captures the color name (which may include spaces)
        """, 
        re.VERBOSE   # Allows for verbose (multi-line) regex with comments
    )
    
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line which is useless.
        
        for line in lines:
            match = re.search(rgx_pattern, line.strip())  # find the values and strip them of whitespace
            if match:
                red, green, blue, colorname = match.groups()  # Extract the four values
                cleaned_line = f'{red}\t{green}\t{blue}\t{colorname}'  # squish them together in new formatting
                rtn_list.append(cleaned_line)
    
    return rtn_list


def main():
    RGB = red_green_blue("src/rgb.txt")
    for rgb in RGB:
        print(rgb)

if __name__ == "__main__":
    main()
