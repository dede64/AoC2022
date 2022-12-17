import re

WIDTH = 7

pieces = [
    [
        ["#", "#", "#", "#"],
    ],
    [
        [".", "#", "."],
        ["#", "#", "#"],
        [".", "#", "."],
    ],
    [
        [".", ".", "#"],
        [".", ".", "#"],
        ["#", "#", "#"],
    ],
    [
        ["#"],
        ["#"],
        ["#"],
        ["#"],
    ],
    [
        ["#", "#"],
        ["#", "#"],
    ],
]

def print_area(area):
    print()
    l = len(area)
    for i in range(l):
        print(area[l - i - 1])

def get_top_occupied_row_index(stack):
    for i in range(len(stack)):
        free = True
        for k in range(WIDTH):
            if stack[i][k] == "#":
                free = False
        if free:
            return i - 1
    return i

def check_pos(stack, rock, next_pos):

    if next_pos[1] < 0 or next_pos[1] + len(rock[0]) > WIDTH:
        return False

    for y in range(len(rock)):
        for x in range(len(rock[0])):
            if rock[y][x] == "#" and stack[next_pos[0] - y][next_pos[1] + x] == "#":
                return False

    return True

def place_rock(stack, rock, next_pos):

    for y in range(len(rock)):
        for x in range(len(rock[0])):
            if rock[y][x] == "#":
                stack[next_pos[0] - y][next_pos[1] + x] = "#"

# Load the file
input_file = open('day17/input_1.txt', 'r')
# input_file = open('day17/input_short.txt', 'r')
line = input_file.read()

winds = [ch for ch in line.strip()]

stack = [["#" for i in range(WIDTH)]]
counter = 0

while counter < 2022:

    # Get rock.
    rock = pieces[counter % len(pieces)]
    counter += 1

    # Append stack with empty rows.
    last_row = get_top_occupied_row_index(stack)
    rock_height = len(rock)
    req_height = last_row + 1 + 3 + rock_height
    stack_height = len(stack)
    for i in range(req_height - stack_height):
        stack.append(["." for k in range(WIDTH)])

    # Add rock to the field.
    rock_pos = [req_height - 1, 2]
    movement_counter = 0

    while True:

        next_pos = [i for i in rock_pos]

        # Move right to left.
        if movement_counter % 2 == 0:
            move = winds.pop(0)
            winds.append(move)

            if move == "<":
                next_pos[1] -= 1
            elif move == ">":
                next_pos[1] += 1

            if check_pos(stack, rock, next_pos):
                rock_pos = next_pos

        else:
            next_pos[0] -= 1

            if check_pos(stack, rock, next_pos):
                rock_pos = next_pos
            else:
                place_rock(stack, rock, rock_pos)
                # print_area(stack)
                break
        
        movement_counter += 1
                


print(get_top_occupied_row_index(stack))