"""
Reads student names and their marks, stores them, and allows querying
for a student's average percentage score.
"""

if __name__ == '__main__':
    # Number of students
    n = int(input())
    student_marks = {}

    # Read student names and their scores
    for _ in range(n):
        name, *line = input().split()  # unpack first as name, rest as scores
        scores = list(map(float, line))
        student_marks[name] = scores

    # Read the student name to query
    query_name = input()
    
    # Calculate average percentage for queried student
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    # Print average formatted to 2 decimal places
    print(f"{average:.2f}")
