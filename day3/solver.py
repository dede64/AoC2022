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

for line in lines:
    line = line.strip()

    # Split the line in half.
    items.append({
        "first_string": line[:len(line)//2],
        "second_string": line[len(line)//2:]
    })

# Convert charws to numbers
for item in items:
    item["f_e"] = []
    item["s_e"] = []

    for ch in item["first_string"]:
        item["f_e"].append(get_char_value(ch))

    for ch in item["second_string"]:
        item["s_e"].append(get_char_value(ch))

# Check which numbers are repeating.
repeating_value = 0

for item in items:
    repeating_items = (set(item["f_e"])).intersection(set(item["s_e"]))
    for i in repeating_items:
        repeating_value += i

print(repeating_value)
