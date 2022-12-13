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

data = re.split("[\n]+",text.strip())

# Add control sequences.
data.append("[[2]]")
data.append("[[6]]")

# Bubble sort the data.
n = len(data)
swapped = False
for i in range(n-1):
    for j in range(0, n-i-1):

        if not compare_values(eval(data[j]), eval(data[j + 1])):
            swapped = True
            data[j], data[j + 1] = data[j + 1], data[j]
        
    if not swapped:
        break

# Find indexes of [[6]] and [[2]]
x = data.index("[[2]]") + 1
y = data.index("[[6]]") + 1

print(x * y)