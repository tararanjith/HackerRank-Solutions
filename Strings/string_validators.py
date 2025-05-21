"""
Checks and prints whether the input string contains at least one alphanumeric character,
alphabetical character, digit, lowercase letter, and uppercase letter.
"""

if __name__ == '__main__':
    # Read input string from the user
    s = input()
    
    # Check if any character is alphanumeric and print the result (True/False)
    print(any(i.isalnum() for i in s))
    
    # Check if any character is alphabetical and print the result
    print(any(i.isalpha() for i in s))
    
    # Check if any character is a digit and print the result
    print(any(i.isdigit() for i in s))
    
    # Check if any character is lowercase and print the result
    print(any(i.islower() for i in s))
    
    # Check if any character is uppercase and print the result
    print(any(i.isupper() for i in s))
