"""
Calculate and print the ratios of positive, negative, and zero elements
in an integer array with precision up to 6 decimal places.
"""

def plusMinus(arr):
    # Count positive, negative and zero elements
    positives = sum(1 for x in arr if x > 0)
    negatives = sum(1 for x in arr if x < 0)
    zeros = sum(1 for x in arr if x == 0)
    total = len(arr)

    # Print ratios with 6 decimal places
    print(f"{positives/total:.6f}")
    print(f"{negatives/total:.6f}")
    print(f"{zeros/total:.6f}")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
