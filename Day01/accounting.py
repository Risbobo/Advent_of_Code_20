import math

myFile = open('input_01.txt', 'r')
lines = myFile.readlines()
data = [int(line) for line in lines]
prod = [x for x in data for y in data if x + y == 2020]
prod_2 = [x for x in data for y in data for z in data if x + y + z == 2020 and y < z]
print(prod)
print(math.prod(prod))
print(prod_2)
print(math.prod(prod_2))