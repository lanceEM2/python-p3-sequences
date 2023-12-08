#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    a, b = 0, 1 # Initializing the first two numbers.
    fibonacci_sequence = [] # empty list to store the fibonacci sequence

    while len(fibonacci_sequence) < length:
    # Starts a while loop that continues until the length of the sequence reaches the specified length
        fibonacci_sequence.append(a)    # Add the current number to the sequence
        a, b = b, a + b     # Update a and b for the next iteration

    print(fibonacci_sequence)  

print_fibonacci(9)      

# The loop continues until the length of fibonacci_sequence reaches 9. At that point, 
# the condition len(fibonacci_sequence) < length becomes False, and the loop exits.