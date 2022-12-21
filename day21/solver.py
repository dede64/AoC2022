# Load the file
input_file = open('day21/input_1.txt', 'r')
# input_file = open('day21/input_short.txt', 'r')
lines = input_file.readlines()

monkeys = {}

for line in lines:

    line = line.strip()
    parts = line.split()

    name = parts[0][:-1]

    if len(parts) == 2:
        monkey = int(parts[1])
    elif len(parts) == 4:
        monkey = {
            "first": parts[1],
            "operand": parts[2],
            "second": parts[3]
        }

    monkeys[name] = monkey


while type(monkeys["root"]) != int:
    for monkey in monkeys:

        m = monkeys[monkey]

        if type(m) == int:
            continue

        a = monkeys[m["first"]]
        b = monkeys[m["second"]]

        if type(a) == int and type(b) == int:
            monkeys[monkey] = int(eval(f'{a} {m["operand"]} {b}'))

print(monkeys["root"])
