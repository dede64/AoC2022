def hsh(x, y):
    return f"{x}-{y}"

# Load the file
# input_file = open('day9/input_1_short.txt', 'r')
input_file = open('day9/input_1.txt', 'r')
lines = input_file.readlines()

result = 0

vis_coords = {}
h_x = h_y = t_x = t_y = 0

for line in lines:

    line = line.strip()
    parts = line.split()

    dir = parts[0]
    cnt = int(parts[1])

    for i in range(cnt):

        if dir == "U":
            h_y += 1
        elif dir == "D":
            h_y -= 1
        elif dir == "L":
            h_x -= 1
        elif dir == "R":
            h_x += 1

        if h_x == t_x and h_y == t_y:
            continue

        # Diagonal move.
        elif h_x != t_x and h_y != t_y:
            
            vect_x = h_x - t_x
            vect_y = h_y - t_y

            if abs(vect_x) + abs(vect_y) > 2:
                t_x += int(vect_x / abs(vect_x))
                t_y += int(vect_y / abs(vect_y))

        # Horizontal move
        elif h_x != t_x:

            # print("hm")
            vect = h_x - t_x
            if abs(vect) > 1:
                t_x += int(vect / abs(vect))

        # Vertical move
        elif h_y != t_y:
            vect = h_y - t_y
            if abs(vect) > 1:
                t_y += int(vect / abs(vect))
        
        vis_coords[hsh(t_x, t_y)] = True

print(len(vis_coords.keys()))