options = {
    "Z": {
        "A": 2 + 6,
        "B": 3 + 6,
        "C": 1 + 6,
    },
    "Y": {
        "A": 1 + 3,
        "B": 2 + 3,
        "C": 3 + 3,
    },
    "X": {
        "A": 3 + 0,
        "B": 1 + 0,
        "C": 2 + 0,
    },
}

# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

score = 0 

for line in lines:

    values = line.split()

    score += options[values[1]][values[0]]

print(score)