# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

for line in lines:
    for i in range(len(line)):

        if i >= 3:

            tmp = set(line[i-4:i])

            if len(tmp) == 4:
                print(i)
                break
