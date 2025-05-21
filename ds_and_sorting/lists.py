"""
Initialize an empty list and perform operations based on input commands:
insert, print, remove, append, sort, pop, reverse.

Each command manipulates the list accordingly.
"""

if __name__ == '__main__':
    n = int(input())  # Number of commands
    lst = []

    for _ in range(n):
        command_line = input().split()
        command = command_line[0]

        if command == "insert":
            index = int(command_line[1])
            element = int(command_line[2])
            lst.insert(index, element)
        elif command == "print":
            print(lst)
        elif command == "remove":
            element = int(command_line[1])
            lst.remove(element)
        elif command == "append":
            element = int(command_line[1])
            lst.append(element)
        elif command == "sort":
            lst.sort()
        elif command == "pop":
            lst.pop()
        elif command == "reverse":
            lst.reverse()
