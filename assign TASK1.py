filename = 'sample.txt'

try:
    print("Reading file content:")
    with open(filename, 'r') as file:
        line_number = 1
        for line in file:
            print("Line", line_number, ":", line.strip())
            line_number += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
