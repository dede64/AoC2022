CONSTANT = 811589153

input_file = open('day20/input_1.txt', 'r')
# input_file = open('day20/input_short.txt', 'r')
# input_file = open('day20/input_short_2.txt', 'r')
lines = input_file.readlines()

numbers = []
id = 0
for line in lines:

    numbers.append({"val": int(line) * CONSTANT, "id": id })
    id += 1

length = len(numbers)

# Iterate the whole list and shift each number.
for k in range(10):
    for i in range(length):
        index = list(map(lambda n: n["id"], numbers)).index(i)
        value = numbers[index]

        value = numbers.pop(index)
        v = value["val"]

        new_index = (index + v) % (length - 1)

        numbers.insert(new_index if new_index else length - 1, value)


# Get index of 0.
o_loc = list(map(lambda n: n["val"], numbers)).index(0)

result = 0
to_check = [1000, 2000, 3000]
for c in to_check:
    result += numbers[(o_loc + c)%length]["val"]

print(result)