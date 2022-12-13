import re

def compare_values(left, right):

    while left != [] and right != []:
        a = left.pop(0)
        b = right.pop(0)

        if type(a) == int and type(b) == int:
            if a < b:
                return True
            elif a == b:
                continue
            elif a > b:
                return False

        if type(a) == int:
            a = [a]
        if type(b) == int:
            b = [b]
        
        result = compare_values(a, b)
        if result is None:
            continue
        else:
            return result
        
        
    if left == [] and right != []:
        return True
    elif right == [] and left != []:
        return False
    else:
        pass


# Load the file
input_file = open('day13/input_1.txt', 'r')
# input_file = open('day13/input_short.txt', 'r')
text = input_file.read()

data = re.split("\n\n",text.strip())

result = 0

for i in range(len(data)):

    line = data[i]

    sides = line.split("\n")
    left = eval(sides[0])
    right = eval(sides[1])

    if compare_values(left=left, right=right):
        result += i + 1

print(result)