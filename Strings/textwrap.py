"""
This script wraps a given string into multiple lines, each with a maximum width specified by `max_width`.
It uses Python's built-in textwrap module for line wrapping.
"""

import textwrap

def wrap(string, max_width):
    # Wrap the string so that each line is at most max_width characters long
    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    # Read input string and maximum width from user
    string, max_width = input(), int(input())
    
    # Call wrap function to get the wrapped string
    result = wrap(string, max_width)
    
    # Print the wrapped string
    print(result)
