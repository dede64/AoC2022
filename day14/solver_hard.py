import re

def create_wall(cave_map, points, max_y):

    last_pt = None

    for pt in points:

        pt = list(map(int, pt))

        # Check for max Y posistion.
        if pt[1] > max_y:
            max_y = pt[1]

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

    return max_y

# Simulates falling sand.
def add_sand(cave_map, s_pos, bottom_layer):

    x = s_pos[0]
    y = s_pos[1]

    while True:
        if y + 1 == bottom_layer:
            cave_map[(x, y)] = "o"
            return True

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
        elif x == s_pos[0] and y == s_pos[1]:
            return False
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

max_y = 0
for line in lines:

    # Apply split regex on the line.
    data = re.split(" -> ", line.strip())
    data = list(map(lambda n: n.split(","), data))
    
    max_y = create_wall(cave_map=cave_map, points=data, max_y=max_y)

bottom_layer = max_y + 2

# Add sand.
counter = 0
while add_sand(cave_map=cave_map, s_pos=(500, 0), bottom_layer=bottom_layer):
    counter += 1

print(counter + 1)
