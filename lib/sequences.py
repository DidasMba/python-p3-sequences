#!/usr/bin/env python3

# lib/sequences.py
def print_fibonacci(length):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence[:length])

# Uncomment the line below if you want to test the function with print_fibonacci(9)
# print_fibonacci(9)

