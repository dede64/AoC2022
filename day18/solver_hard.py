import re
import sys

# Change recursion limit
sys.setrecursionlimit(100000)

DIRS = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]

def check_sides(cubes, cube):

    visible = 6

    for d in DIRS:
        if (cube[0] + d[0], cube[1] + d[1], cube[2] + d[2]) in cubes:
            visible -= 2

    return visible

def is_valid_coord(coord):
    if coord[0] < min_coord[0] or coord[0] > max_coord[0] \
            or coord[1] < min_coord[1] or coord[1] > max_coord[1] \
            or coord[2] < min_coord[2] or coord[2] > max_coord[2]:
        return False
    return True

def expand(where, inv_cubes):

    inv_faces = check_sides(cubes=inv_cubes, cube=where)

    inv_cubes.add(where)

    for d in DIRS:
        coord = (where[0] + d[0], where[1] + d[1], where[2] + d[2])
        if not is_valid_coord(coord):
            continue
        if coord not in cubes and coord not in inv_cubes:
            inv_faces += expand(coord, inv_cubes)
    return inv_faces

# Load the file
input_file = open('day18/input_1.txt', 'r')
# input_file = open('day18/input_short.txt', 'r')
# input_file = open('day18/input_short_2.txt', 'r')
lines = input_file.readlines()

# Load the cubes
cubes = set()
for line in lines:
    cube = tuple(map(int, re.split("[,]",line.strip())))
    if cube not in cubes:
        cubes.add(cube)

min_coord = (
    min(map(lambda n: n[0], cubes)) - 1,
    min(map(lambda n: n[1], cubes)) - 1,
    min(map(lambda n: n[2], cubes)) - 1
)
max_coord = (
    max(map(lambda n: n[0], cubes)) + 1,
    max(map(lambda n: n[1], cubes)) + 1,
    max(map(lambda n: n[2], cubes)) + 1
)

# Create negative mold of the cubes.
inv_cubes = set()
inv_faces = expand(min_coord, inv_cubes)

# Substract mold outside area from the total faces.
x = max_coord[0] - min_coord[0] + 1
y = max_coord[1] - min_coord[1] + 1
z = max_coord[2] - min_coord[2] + 1
inv_faces -= 2 * (x * y  +  y * z  + z * x)

print(inv_faces)
