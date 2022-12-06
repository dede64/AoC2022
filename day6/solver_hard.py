# Load the file
input_file = open('input_1.txt', 'r')
lines = input_file.readlines()

for line in lines:
    for i in range(len(line)):

        if i >= 13:

            tmp = set(line[i-14:i])

            if len(tmp) == 14:
                print(i)
                break
