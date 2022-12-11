MEASURE_VALUES = [20, 60, 100, 140, 180, 220]

def check_cycle(cycle, X, measured_data):
    if cycle in MEASURE_VALUES:

        print(f"{cycle}: {X}")
        measured_data.append(cycle * X)

    return measured_data

# Load the file
input_file = open('day10/input_1.txt', 'r')
# input_file = open('day10/input_short.txt', 'r')
# input_file = open('day10/input_extra_short.txt', 'r')
lines = input_file.readlines()

result = 0

X = 1
cycle_number = 0
measured_data = []


#########################
# Regex split.
for line in lines:

    line = line.strip()

    # Apply split regex on the line.
    data = line.split()

    if len(data) == 1:

        cycle_number += 1
        measured_data = check_cycle(cycle_number, X, measured_data)

    else:

        cycle_number += 1
        measured_data = check_cycle(cycle_number, X, measured_data)

        cycle_number +=1
        measured_data = check_cycle(cycle_number, X, measured_data)

        X += int(data[1])

print(f"end cycle: {cycle_number}\n")
print(measured_data)
print(sum(measured_data))