#!/usr/bin/env python3
import sys

def file_extensions(filename):
    no_extension = []
    extensions_dict = {}

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if "." in line:
                parts = line.split(".")
                extension = parts[-1]  # get the last part or extension
                file_name = line

                # make an empty key for first time
                if extension not in extensions_dict:
                    extensions_dict[extension] = []
                extensions_dict[extension].append(file_name)
            else:
                no_extension.append(line)  # Files with no extensions
    return (no_extension, extensions_dict)

def main():
    filename = "src/filenames.txt"
    no_extension, extensions_dict = file_extensions(filename)

    print(f"{len(no_extension)} files with no extension")
    
    for ext in extensions_dict.keys():
        print(f"{ext} {len(extensions_dict[ext])}")

if __name__ == "__main__":
    main()
