import random

a = 7
matrix = []
for i in range(a):
    matrix.append([random.randint(0, 99) for j in range(a)])
    print(*matrix[i])


print("\n", "Матрица с нулями", "\n")

for i in range(a):
    matrix[0][i] = 0
    matrix[6][i] = 0
    matrix[i][0] = 0
    matrix[i][6] = 0

def PRM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


print(PRM(matrix))