#!/usr/bin/env python3

import re

# Works only when inside e22_file_listing
def file_listing(filename="src/listing.txt"):
    rtn_list = []
    regx_pattern = re.compile(
        r"""
        \s+          # allows for one or more whitespace characters
        (\d+)        # One or more digits (file size)
        \s+          # allows for one or more whitespace characters
        ([A-Za-z]{3})# Exactly three letters (month)
        \s+          # allows for one or more whitespace characters
        (\d{1,2})    # One or two digits (day of the month)
        \s+          # allows for one or more whitespace characters
        (\d{2})      # Exactly two digits (hour)
        :            # Colon separator between hour and minute
        (\d{2})      # Exactly two digits (minute)
        \s+          # allows for one or more whitespace characters
        (.+)         # allows for one or any character (filename)
        """, 
        re.VERBOSE
    )
    
    with open(filename, 'r') as file:
        for line in file:
            match = regx_pattern.search(line)
            if match:
                size = int(match.group(1))
                month = match.group(2)
                day = int(match.group(3))
                hour = int(match.group(4))
                minute = int(match.group(5))
                filename = match.group(6)

                # Append as tuples
                rtn_list.append((size, month, day, hour, minute, filename))
        
    return rtn_list

def main():
    prnt_example = file_listing("src/listing.txt")
    for i in prnt_example:
        print(i)

if __name__ == "__main__":
    main()
