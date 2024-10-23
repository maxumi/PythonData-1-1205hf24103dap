#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    # Attempt to convert the line to a float.
                    numbers.append(float(line.strip()))
                except ValueError:
                    # Skip any lines that cannot be converted to a float.
                    print(f"Warning: '{line.strip()}' is not a valid number in file '{filename}'.")
        
        if len(numbers) == 0:
            raise ValueError("The file contains no valid numbers to process.")
        
        sum_of_numbers = sum(numbers)
        average = sum_of_numbers / len(numbers)
        # If a single number exists, stdev will return 0.
        standard_deviation = statistics.stdev(numbers) if len(numbers) > 1 else 0.0

        return (sum_of_numbers, average, standard_deviation)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{filename}' not found.")
    except ValueError as ve:
        raise ValueError(f"Value Error: {ve}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while processing the file: {e}")

def main():
    args = sys.argv[1:]  # Skip the first argument, which is the script name.
    for argument in args:
        # error handling incase the function gets an error.
        try:
            sum_value, average, stddev = summary(argument)
            print(f"File: {argument} Sum: {sum_value:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
