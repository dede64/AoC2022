import re

# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

count = 0

for line in lines:

    # Convert input to the list of ints.
    all = re.split("[,\-\n]",line.strip())
    all = [int(i) for i in all]

    # Check if ranges overlap.
    if all[0] <= all[2] and all[1] >= all[3]:
        count += 1
    elif all[2] <= all[0] and all[3] >= all[1]:
        count += 1
    elif all[0] <= all[2] and all[1] >= all[2]:
        count += 1
    elif all[0] <= all[3] and all[1] >= all[3]:
        count += 1

print(count)