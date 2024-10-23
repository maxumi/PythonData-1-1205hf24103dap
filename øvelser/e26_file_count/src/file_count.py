#!/usr/bin/env python3

import sys

def file_count(filename):
    try:
        with open(filename, 'r') as file:
            file_lines = file.readlines()
            total_lines = len(file_lines)
            word_count = 0
            character_count = 0

            for line in file_lines:
                words = line.split()
                word_count += len(words)
                character_count += len(line)

            return (total_lines, word_count, character_count)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read file '{filename}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while processing '{filename}': {e}")
        return None


def main():
    arugments = sys.argv[1:]
    for filename in arugments:
        result = file_count(filename)
        if result is not None:
            lines, words, characters = result
            print(f"{lines}\t{words}\t{characters}\t{filename}")

if __name__ == "__main__":
    main()
