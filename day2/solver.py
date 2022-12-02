options = [
    ("A", "Y", 6, 2),
    ("B", "Z", 6, 3), 
    ("C", "X", 6, 1),
    ("A", "X", 3, 1),
    ("B", "Y", 3, 2), 
    ("C", "Z", 3, 3),
    ("A", "Z", 0, 3),
    ("B", "X", 0, 1), 
    ("C", "Y", 0, 2),
]

# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

score = 0 

for line in lines:

    values = line.split()

    for option in options:
        if values[1] == option[1]:
            if values[0] == option[0] and values[1] == option[1]:
                score += option[2]
                score += option[3]

print(score)