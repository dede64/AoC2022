import re

def manh_dst(pos_1, pos_2):
    return abs(pos_2[0] - pos_1[0]) + abs(pos_2[1] - pos_1[1])

def get_y_cut(sensor, y):

    range = manh_dst(sensor[:2], sensor[2:])

    scan_dist = abs(sensor[1] - y)

    if scan_dist > range:
        return None

    df = range - scan_dist

    r = [sensor[0] - df, sensor[0] + df]

    # Remove beacon from the range.
    if sensor[3] == y:
        if sensor[2] == r[0]:
            r[0] += 1
        if sensor[2] == r[1]:
            r[1] -= 1
        if r[1] < r[0]:
            return None
    return r

# Load the file
input_file = open('day15/input_1.txt', 'r')
# input_file = open('day15/input_short.txt', 'r')
lines = input_file.readlines()

sensors = []



#########################
# Regex split.
for line in lines:

    # Apply match regex on the line.
    data = list(map(int, re.match("Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)", line.strip()).groups()))
    sensors.append(data)

scan_y = 2000000
# scan_y = 10

cuts = []
for sensor in sensors:
    cut = get_y_cut(sensor=sensor, y=scan_y)
    if cut:
        cuts.append(cut)

# Sort ranges by min x
cuts = sorted(cuts, key=lambda n: n[0])

# Merge cuts ranges.
merged_cuts = []

a = None
b = None
for cut in cuts:
    if not a:
        a = cut[0]
    if not b:
        b = cut[1]

    if cut[0] <= b + 1 and cut[1] > b:
        b = cut[1]
    elif cut[0] > b + 1:
        merged_cuts.append([a, b])
        a = cut[0]
        b = cut[1]

if a and b:
    merged_cuts.append([a, b])

dst = 0
for cut in merged_cuts:
    dst += cut[1] - cut[0] + 1

print(dst)