import re

ROUNDS = 20

class Monkey :


    def __init__(self, id, items, operation, operation_val, divisible, true_comp, false_comp):

        self.id = id
        self.items = items
        self.operation = operation
        self.operation_val = operation_val
        self.divisible = divisible
        self.true_comp = true_comp
        self.false_comp = false_comp
        self.throws = 0


    def process_items(self, monkeys):

        for item in self.items:

            if self.operation == "+":
    
                if self.operation_val == "old":
                    new_val = item + item
                else:
                    new_val = item + int(self.operation_val)

            elif self.operation == "*":

                if self.operation_val == "old":
                    new_val = item * item
                else:
                    new_val = item * int(self.operation_val)

            new_val = new_val // 3

            # Throw to the next monkey.
            if new_val % self.divisible == 0:
                monkeys[self.true_comp].items.append(new_val)

                print(f"{self.id}: {item} -> {new_val} ({self.true_comp})")
            else:
                monkeys[self.false_comp].items.append(new_val)

                print(f"{self.id}: {item} -> {new_val} ({self.false_comp})")

            self.throws += 1

        self.items = []

    def __str__(self):
        return f"Monkey: {self.id} {self.items} {self.throws}"



# Load the file
input_file = open('day11/input_1.txt', 'r')
# input_file = open('day11/input_short.txt', 'r')
text = input_file.read()

# Load monkeys from file.
monkey_ids = list(map(int, re.findall(r'Monkey ([\d]+):', text)))
starting_items_lines = re.findall(r'Starting items: ([\d\ ,]+)\n', text)
starting_items = list(map(lambda n: list(map(int, n.split(","))), starting_items_lines))
operations_lines = re.findall(r'Operation: new = old ([+*]) ([\d]+|old)\n', text)
operations = list(map(lambda n: n[0], operations_lines))
operation_values = list(map(lambda n: n[1], operations_lines))
divisible = list(map(int, re.findall(r'Test: divisible by ([\d]+)\n', text)))
true_comp = list(map(int, re.findall(r'If true: throw to monkey ([\d]+)', text)))
false_comp = list(map(int, re.findall(r'If false: throw to monkey ([\d]+)', text)))

# Create monkeys.
monkeys = []
for i in range(len(monkey_ids)):

    monkeys.append(
        Monkey(
            id=monkey_ids[i],
            items=starting_items[i],
            operation=operations[i],
            operation_val=operation_values[i],
            divisible=divisible[i],
            true_comp=true_comp[i],
            false_comp=false_comp[i]
        )
    )

# Rounds
for i in range(ROUNDS):

    for monkey in monkeys:
        monkey.process_items(monkeys)

    for monkey in monkeys:
        print(monkey)

    print()


print(list(map(lambda n: n.throws, monkeys)))