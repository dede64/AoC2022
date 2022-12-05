import re

def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

def print_stacks(stacks):
    for i in stacks:
        print(i)

def move_item(stacks, cnt, f, t):

    carry = []

    for k in range(cnt):

        carry.append(stacks[f].pop(0))
        
    stacks[t] = carry + stacks[t]
    
    return stacks

def convert_stacks(stacks):

    new = []
    for i in range(len(stacks[0])):
        new.append([])

        for j in range(len(stacks)):
            new[i].append(stacks[j][i])

    # Clear spaces.
    for i in range(len(new)):
        while(new[i][0] == "@"):
            new[i].pop(0)
    return new

# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

stage = 0

stacks = []

for line in lines:

    if has_numbers(line) and stage != 1:
        stage = 1

        stacks = convert_stacks(stacks)

    if stage == 0:

        line = line.replace("    ", "[@]")
        line = line.replace(" ", "")

        # Apply split regex on the line.
        data = re.split("[\[\]]",line.strip())

        new_data = []
        for element in data:
            if element != "":
                new_data.append(element)
        stacks.append(new_data)

    elif stage == 1:
        if "move" not in line:
            continue
        data = line.split()
        stacks = move_item(stacks=stacks, cnt=int(data[1]), f=int(data[3]) - 1, t=int(data[5]) - 1)

print_stacks(stacks)