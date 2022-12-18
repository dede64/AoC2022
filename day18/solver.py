import re

def check_sides(cubes, cube):

    visible = 6

    dirs = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]

    for d in dirs:
        if (cube[0] + d[0], cube[1] + d[1], cube[2] + d[2]) in cubes:
            visible -= 2

    return visible

# Load the file
input_file = open('day18/input_1.txt', 'r')
# input_file = open('day18/input_short.txt', 'r')
lines = input_file.readlines()

faces = 0

cubes = set()

for line in lines:

    # Apply split regex on the line.
    cube = tuple(map(int, re.split("[,]",line.strip())))

    # Check if cube isnt duuplicate.
    if cube not in cubes:

        # Check sides.
        faces += check_sides(cubes=cubes, cube=cube)

        # Add cube to cubes.
        cubes.add(cube)

print(faces)
