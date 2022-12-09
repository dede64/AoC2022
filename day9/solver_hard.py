ROPE_LENGTH = 10

def hsh(x, y):
    return f"{x}-{y}"

def get_coords(h, t):

    if h["x"] == t["x"] and h["y"] == t["y"]:
        return t

    # Diagonal move.
    elif h["x"] != t["x"] and h["y"] != t["y"]:
        
        vect_x = h["x"] - t["x"]
        vect_y = h["y"] - t["y"]

        if abs(vect_x) + abs(vect_y) > 2:
            t["x"] += int(vect_x / abs(vect_x))
            t["y"] += int(vect_y / abs(vect_y))

    # Horizontal move
    elif h["x"] != t["x"]:

        vect = h["x"] - t["x"]
        if abs(vect) > 1:
            t["x"] += int(vect / abs(vect))

    # Vertical move
    elif h["y"] != t["y"]:
        vect = h["y"] - t["y"]
        if abs(vect) > 1:
            t["y"] += int(vect / abs(vect))

    return t


# Load the file
# input_file = open('day9/input_1_short.txt', 'r')
# input_file = open('day9/input_example.txt', 'r')
input_file = open('day9/input_1.txt', 'r')
lines = input_file.readlines()

result = 0

vis_coords = {}

knots = [{"x":0, "y":0} for i in range(ROPE_LENGTH)]

for line in lines:

    line = line.strip()
    parts = line.split()

    dir = parts[0]
    cnt = int(parts[1])

    for i in range(cnt):

        if dir == "U":
            knots[0]["y"] += 1
        elif dir == "D":
            knots[0]["y"] -= 1
        elif dir == "L":
            knots[0]["x"] -= 1
        elif dir == "R":
            knots[0]["x"] += 1

        # Iterate knots
        for j in range(1, ROPE_LENGTH):
            knots[j] = get_coords(knots[j-1], knots[j])
        
        last_knot = knots[ROPE_LENGTH - 1]
        if not(len(vis_coords.keys()) != 0 and last_knot["x"] == 0 and last_knot["y"] == 0):
            vis_coords[hsh(last_knot["x"], last_knot["y"])] = True


print(len(vis_coords.keys()))