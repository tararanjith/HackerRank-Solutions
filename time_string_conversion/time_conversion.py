"""
Convert time from 12-hour AM/PM format to 24-hour format.
"""

def timeConversion(s):
    period = s[8:]            # Extract AM/PM
    hour = int(s[0:2])        # Extract hour part as integer
    rest = s[3:8]             # Extract minutes and seconds

    # Convert hour based on period
    if period == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    # Return formatted time in 24-hour format
    return f"{hour:02d}:{rest}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
