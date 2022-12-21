# Load the file
input_file = open('day21/input_1.txt', 'r')
# input_file = open('day21/input_short.txt', 'r')
lines = input_file.readlines()

monkeys = {}

for line in lines:

    line = line.strip()
    parts = line.split()

    name = parts[0][:-1]

    if name == "humn":
        monkey = {
            "first": "xxxxxxx",
            "operand": "x",
            "second": "yyyyyyyy"
        }
    elif len(parts) == 2:
        monkey = int(parts[1])
    elif len(parts) == 4:
        monkey = {
            "first": parts[1],
            "operand": parts[2],
            "second": parts[3]
        }

    monkeys[name] = monkey


did_change = True
while did_change:

    did_change = False

    for monkey in monkeys:

        if monkey == "humn":
            continue

        m = monkeys[monkey]

        if type(m) == int:
            continue

        a = monkeys[m["first"]]
        b = monkeys[m["second"]]

        if type(a) == int and type(b) == int:
            
            monkeys[monkey] = int(eval(f'{a} {m["operand"]} {b}'))
            did_change = True

# Go from the root down to the humn node.
current = monkeys["root"]
value = monkeys[current["first"]] if type(monkeys[current["first"]]) == int else monkeys[current["second"]]
current_name = current["first"] if type(monkeys[current["first"]]) == dict else current["second"]
current = monkeys[current_name]

while True:

    if current_name == "humn":
        break

    a = current["first"]
    b = current["second"]

    x = monkeys[a]
    y = monkeys[b]

    # Right side of the equation is real number.
    if type(y) == int:

        if current["operand"] == "+":
            value = value - y
        elif current["operand"] == "-":
            value = value + y
        elif current["operand"] == "*":
            value = value / y
        elif current["operand"] == "/":
            value = value * y
        current_name = a

    # Left side of the equation is real number.
    elif type(x) == int:

        if current["operand"] == "+":
            value = value - x
        elif current["operand"] == "-":
            value = x - value
        elif current["operand"] == "*":
            value = value / x
        elif current["operand"] == "/":
            value = x / value
        current_name = b

    current = monkeys[current_name]
    value = int(value)

print(value)
