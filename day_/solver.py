import re

# Load the file
input_file = open('dayX/input_1.txt', 'r')
lines = input_file.readlines()

result = 0

#########################
# Regex split.
for line in lines:

    # Apply split regex on the line.
    data = re.split("[,\-\n]",line.strip())

########################
# Load 2D area.
area = []
for line in lines:

    line = line.strip()
    row = []

    for ch in line: 
        row.append(ch)
    
    area.append(row)

    


print(result)