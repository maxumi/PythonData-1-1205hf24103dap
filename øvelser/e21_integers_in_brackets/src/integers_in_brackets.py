#!/usr/bin/env python3
import re

def integers_in_brackets(s: str):
    # "\[" matches the opening bracket "["
    # "\s*" matches any whitespaces (or none) after the bracket
    # "[+-]?" optionally matches a "+" or "-" sign before the number
    # "\d+" matches one or more digits (0-9)
    # "\s*\]" matches any whitespaces (or none) before the closing bracket "]"
    # "(" and ")" is for getting it without the brackets(else you get with brackets)
    pattern = r"\[\s*([+-]?\d+)\s*\]"
    matches = re.findall(pattern, s)
    # Convert matches from strings to integers
    return [int(match) for match in matches]

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
