def check_tree(x, y, trees):

    x_length = len(trees)
    y_length = len(trees[0])

    height = trees[x][y]

    a = b = c = d = 0

    # Check <x direction
    for i in range(0, x):
        val = trees[x - i - 1][y]
        a = i + 1
        if val >= height:
            break

    # Check x> direction
    for i in range(x + 1, x_length):
        val = trees[i][y]
        b = i - x
        if val >= height:
            break

    # Check vy direction
    for i in range(0, y):
        val = trees[x][y - i - 1]
        c = i + 1
        if val >= height:
            break

    # Check ^y direction
    for i in range(y + 1, y_length):
        val = trees[x][i]
        d = i - y
        if val >= height:
            break

    return a * b * c * d
        

trees=[]

# Load the file
input_file = open('day8/input_1.txt', 'r')
lines = input_file.readlines()

result = 0

for line in lines:

    tmp = []

    line = line.strip()

    for ch in line:
        tmp.append(int(ch))
    trees.append(tmp)

max_score = 0

for x in range(len(trees)):
    for y in range(len(trees[0])):
        tmp = check_tree(x, y, trees=trees)
        if tmp > max_score:
            max_score = tmp

print(max_score)