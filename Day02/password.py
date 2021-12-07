import re

myFile = open('input_02.txt', 'r')
lines = myFile.readlines()
right_1 = 0
right_2 = 0
for line in lines:
    process = re.split("-| |: ", line)
    lower = int(process[0])
    higher = int(process[1])
    control = process[2]
    password = process[3].strip()
    if password.count(control) in range(lower, higher + 1):
        right_1 += 1
    if (password[lower - 1] == control) ^ (password[higher - 1] == control):
        right_2 += 1

print(right_1)
print(right_2)
