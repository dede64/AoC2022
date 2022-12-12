class Point:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.dst = -1
        self.processed = False

# Load the file
input_file = open('day12/input_1.txt', 'r')
# input_file = open('day12/input_short.txt', 'r')
lines = input_file.readlines()

########################
# Load 2D area.
area = []
height = 0

ends = []

for line in lines:

    line = line.strip()
    row = []

    width = 0
    for ch in line:

        if ch == "S" or ch == "a":
            point = Point(
                x=width,
                y=height,
                value=1
            )
            ends.append(point)
            row.append(point)
            start = point

        elif ch == "E":
            point = Point(
                x=width,
                y=height,
                value=26
            )
            row.append(point)
            end = point
        else:
            point = Point(
                x=width,
                y=height,
                value=ord(ch) - ord('a') + 1
            )
            row.append(point)
        width += 1
    
    area.append(row)
    height += 1

def get_neighbours(area: list[list[Point]], point: Point, queue: list[Point]):

    width = len(area[0])
    height = len(area)
    x = point.x
    y = point.y
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    for direction in directions:
        xx = x + direction[1]
        yy = y + direction[0]

        if xx < 0 or xx >= width or yy < 0 or yy >= height:
            continue

        pt = area[yy][xx]
        if pt.dst != -1:
            continue

        if pt.value >= point.value - 1:
            pt.dst = point.dst + 1
            queue.append(pt)



def bfs(start: Point, area: list[list[Point]]):

    start.dst = 0
    queue = [start]

    while queue:

        e = queue.pop(0)

        # Point hasn't been visited yet.
        if not e.processed:

            # Add neignours to the queue.
            get_neighbours(area=area, point=e, queue=queue)

            e.processed = True

# BFS end to starts.
bfs(start=end, area=area)

print(min(map(lambda n : n.dst if n.dst > -1 else 9999999999, ends)))
