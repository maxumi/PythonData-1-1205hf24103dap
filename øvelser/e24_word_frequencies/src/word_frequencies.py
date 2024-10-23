#!/usr/bin/env python3
import string

def word_frequencies(filename="src/alice.txt"):
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()

            for word in words:
                stripped_word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if stripped_word in word_count:
                    word_count[stripped_word] += 1
                else:
                    word_count[stripped_word] = 1
    return word_count

def main():
    frequencies = word_frequencies()
    for word in sorted(frequencies.keys()):
        print(f"{word}: {frequencies[word]}")

if __name__ == "__main__":
    main()
