def check_tree(x, y, trees):

    x_length = len(trees)
    y_length = len(trees[0])

    height = trees[x][y]

    # Check <x direction
    tmp = -1
    for i in range(0, x):
        val = trees[i][y]
        if val > tmp:
            tmp = val        

    if tmp < height:
        return False

    # Check x> direction
    tmp = -1
    for i in range(x + 1, x_length):
        val = trees[i][y]
        if val > tmp:
            tmp = val        

    if tmp < height:
        return False

    # Check vy direction
    tmp = -1
    for i in range(0, y):
        val = trees[x][i]
        if val > tmp:
            tmp = val        

    if tmp < height:
        return False

    # Check ^y direction
    tmp = -1
    for i in range(y + 1, y_length):
        val = trees[x][i]
        if val > tmp:
            tmp = val        

    if tmp < height:
        return False

    return True
        

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

cnt = 0

for x in range(len(trees)):
    for y in range(len(trees[0])):
        if not check_tree(x, y, trees=trees):
            cnt += 1

print(cnt)