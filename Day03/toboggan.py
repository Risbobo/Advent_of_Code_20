import numpy as np

myFile = open('input_03.txt', 'r')
lines = myFile.readlines()

count_tree = [0]*5
x_pos = np.array([0]*3)
for l, line in enumerate(lines):
    for i, x in enumerate(x_pos):
        if line[x % len(line.strip())] == '#':
            count_tree[i] += 1
    x_pos += np.array([1, 3, 5, 7, 0])
    if l % 2 == 1:
        True

print(x_pos)
print(count_tree)