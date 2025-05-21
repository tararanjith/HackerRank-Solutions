"""
This script capitalizes the first letter of each word in the input string.
It reads a string from input, processes it, and outputs the capitalized version.
"""

def solve(s):
    # Convert the input string to a list of characters
    s = list(s)
    
    # Capitalize the first character of the string
    s[0] = s[0].upper()
    
    # Iterate over the string starting from the second character
    for i in range(1, len(s)):
        # If the previous character is a space, capitalize the current character
        if s[i-1] == ' ':
            s[i] = s[i].upper()
    
    # Join the list back into a string and return the result
    return ''.join(s)

if __name__ == '__main__':
    import os
    # Open a file to write the output (path provided by environment variable OUTPUT_PATH)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input string from standard input
    s = input()

    # Call the solve function with the input string
    result = solve(s)

    # Write the result to the output file with a newline
    fptr.write(result + '\n')

    # Close the file
    fptr.close()
