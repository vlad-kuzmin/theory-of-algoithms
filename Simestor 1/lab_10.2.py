from pprint import pprint
import random

a = 5
matrix = []
idx_row = 2
idx_col = int(input("ВВЕДИТЬ НОМЕР УДАЛЯЕМОГО СТОЛБЦА: "))-1



for i in range(a):
    matrix.append([random.randint(0, 99) for j in range(a)])


def PRM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()

pprint(PRM(matrix))

rows = len(matrix)
for i in range(rows):
    _ = matrix[i].pop(idx_col)

pprint(PRM(matrix))
