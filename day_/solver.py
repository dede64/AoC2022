import re

# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

result = 0

for line in lines:

    # Apply split regex on the line.
    data = re.split("[,\-\n]",line.strip())

    ....


return result