"""
Reads first and last name from input and prints a greeting message.
Demonstrates basic input, function parameters, and formatted string output.
"""

def print_full_name(first, last):
    # Print the greeting with first and last names passed as arguments
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    # Take first and last name input from user
    first_name = input()
    last_name = input()
    
    # Call the function with user inputs
    print_full_name(first_name, last_name)
