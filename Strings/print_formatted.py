"""
This script prints the decimal, octal, hexadecimal (uppercase), and binary
representations of numbers from 1 up to a given number `n`. All values are
right-aligned to the width of the binary representation of `n`.
"""

def print_formatted(number):
    # Calculate the width needed for alignment based on binary length of `number`
    width = len(bin(number)[2:])
    
    # Loop through each number from 1 to `number`
    for i in range(1, number + 1):
        # Print decimal, octal, hexadecimal, and binary representations,
        # each right-justified by the calculated width
        print(
            f"{str(i).rjust(width)} "
            f"{oct(i)[2:].rjust(width)} "
            f"{hex(i)[2:].upper().rjust(width)} "
            f"{bin(i)[2:].rjust(width)}"
        )


if __name__ == '__main__':
    # Read input number from user
    n = int(input())
    # Call the function to print formatted numbers
    print_formatted(n)
