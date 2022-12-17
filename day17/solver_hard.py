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
turns = 0

repeats = []

while len(repeats) < 4:

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

            turns += 1
            if turns % len(winds) == 0:
                repeats.append({"height": get_top_occupied_row_index(stack), "rocks": counter})
                # print(f"{get_top_occupied_row_index(stack)} {counter}")

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

if repeats[-1]["height"] - repeats[-2]["height"] != repeats[-2]["height"] - repeats[-3]["height"]:
    print("ERROR")
if repeats[-1]["rocks"] - repeats[-2]["rocks"] != repeats[-2]["rocks"] - repeats[-3]["rocks"]:
    print("ERROR")

target_rocks = 1000000000000
target_rocks -= repeats[0]["rocks"]

repeat_height = repeats[-1]["height"] - repeats[-2]["height"]
repeat_rocks = repeats[-1]["rocks"] - repeats[-2]["rocks"]

section_repeates = target_rocks // repeat_rocks
target_rest = repeats[0]["rocks"] + (target_rocks % repeat_rocks)

winds = [ch for ch in line.strip()]
stack = [["#" for i in range(WIDTH)]]
counter = 0
while counter < target_rest:

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
                break
        
        movement_counter += 1

rest_height = get_top_occupied_row_index(stack)

result = rest_height + section_repeates * repeat_height
print(result)