import re

def create_wall(cave_map, points):

    last_pt = None

    for pt in points:

        pt = list(map(int, pt))

        if last_pt:

            # Create wall from lastpt to pt.
            # Horizontal wall:
            if pt[0] != last_pt[0]:
                mn = min([pt[0], last_pt[0]])
                mx = max([pt[0], last_pt[0]])
                y = pt[1]

                for x in range(mn, mx + 1):
                    cave_map[(x,y)] = "#"

            # Vertical wall:
            elif pt[1] != last_pt[1]:
                mn = min([pt[1], last_pt[1]])
                mx = max([pt[1], last_pt[1]])
                x = pt[0]

                for y in range(mn, mx + 1):
                    cave_map[(x,y)] = "#"
        last_pt = pt

def add_sand(cave_map, s_pos):

    x = s_pos[0]
    y = s_pos[1]

    while True:

        if y > 1000:  # TODO use max y
            return False

        elif cave_map.get((x, y + 1), None) is None: 
            y += 1
            continue
        elif cave_map.get((x - 1, y + 1), None) is None:
            x -= 1
            y += 1
            continue
        elif cave_map.get((x + 1, y + 1), None) is None:
            x += 1
            y += 1
            continue
        else:
            cave_map[(x, y)] = "o"
            return True


# Load the file
input_file = open('day14/input_1.txt', 'r')
# input_file = open('day14/input_short.txt', 'r')
lines = input_file.readlines()

cave_map = {}

#########################
# Regex split.
for line in lines:

    # Apply split regex on the line.
    data = re.split(" -> ", line.strip())
    data = list(map(lambda n: n.split(","), data))
    
    create_wall(cave_map=cave_map, points=data)


# Add sand.
counter = 0
while add_sand(cave_map=cave_map, s_pos=(500, 0)):
    counter += 1

print(counter)
