"""
Calculate and print the minimum and maximum sum of exactly four of five integers in the list.
"""

def miniMaxSum(arr):
    # Sort the array to easily pick min and max sums
    arr.sort()
    
    # Minimum sum is sum of first four elements
    min_sum = sum(arr[:4])
    
    # Maximum sum is sum of last four elements
    max_sum = sum(arr[1:])
    
    # Print results separated by space
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
