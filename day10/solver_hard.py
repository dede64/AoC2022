MEASURE_VALUES = [20, 60, 100, 140, 180, 220]
S_WIDTH = 3
WIDTH = 40
HEIGHT = 6

def update_screen(screen, cycle, pos):
    r_pos = cycle % WIDTH

    if pos - 1 == r_pos or pos == r_pos or pos + 1 == r_pos:
        screen[cycle // WIDTH][cycle % WIDTH] = "#"

    return screen

def print_screen(screen):

    for row in screen:
        r = ""
        for ch in row:
            r = f"{r}{ch}"

        print(r)

# Load the file
input_file = open('day10/input_1.txt', 'r')
# input_file = open('day10/input_short.txt', 'r')
# input_file = open('day10/input_extra_short.txt', 'r')
lines = input_file.readlines()

result = 0

cycle_number = -1
measured_data = []

pos = 1

screen = [["." for i in range(WIDTH)] for i in range(HEIGHT)]


#########################
# Regex split.
for line in lines:

    line = line.strip()

    # Apply split regex on the line.
    data = line.split()

    if len(data) == 1:

        cycle_number += 1
        screen = update_screen(screen, cycle_number, pos)

    else:

        cycle_number += 1
        screen = update_screen(screen, cycle_number, pos)

        cycle_number +=1
        screen = update_screen(screen, cycle_number, pos)

        pos += int(data[1])

print_screen(screen)