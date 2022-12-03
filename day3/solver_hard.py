def get_char_value(ch):
    """
    Converts char to number a=1 z=26 A=27 Z=52.
    """

    if ord(ch) >= 97:
        return ord(ch) - 96

    return ord(ch) - 64 + 26

# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

items = []

# Load each line converted to char numbers.
for line in lines:
    line = line.strip()

    res = []
    for ch in line:
        res.append(get_char_value(ch))
    items.append(res)


# Get repeated value in each triplet.
repeating_value = 0

for k in range(len(items)//3):
    inters1 = (set(items[3*k + 0])).intersection(set(items[3*k + 1]))
    inters = (inters1).intersection(set(items[3*k + 2]))
    for i in inters:
        repeating_value += i

print(repeating_value)