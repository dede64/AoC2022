max_calories = [0 for i in range(3)]

# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

# Iterate the lines and get the block with most calories in total
tmp_calories = 0
for line in lines:

    # Strip number from the newline char at the end.
    line = line.strip()

    # Check if it is a end of a block.
    if line == "":
        if tmp_calories > max_calories[0]:
            max_calories.append(tmp_calories)
            max_calories.sort()
            max_calories.pop(0)

        tmp_calories = 0

    else:
        tmp_calories += int(line)

# Backup, if there is no newline at the end.
if tmp_calories > max_calories[0]:
    max_calories.append(tmp_calories)
    max_calories.sort()
    max_calories.pop(0)

print(max_calories)
print(sum(max_calories))
