"""
Reads a list of integers from input and converts them into a tuple.
Demonstrates basic tuple creation and immutability.
"""

if __name__ == '__main__':
    # Read the number of elements (not used directly but part of input format)
    n = int(input())
    
    # Read integers from input and convert to a tuple
    integer_list = tuple(map(int, input().split()))
    
    # Print the tuple (optional, depending on the problem)
    print(integer_list)
