import numpy as np

matrix = [[1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]]
n = 2
m = 2
s1 = []
s2 = []
o = 0
b = np.asarray(matrix)
ds1 = 0
ds2 = 0
flag = 0
# for i in range(n):
#     matrix.append([2] * m)



for row in matrix:  # СЧЕТ СТРОК И ЗАПИСЬ В СПИСОК
    s1.append(sum(row))


def sumColumn(m, column):   # ФУНКЦИЯ СЧЕТА СТОЛБЦОВ
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total


while o < n:    # СЧЕТ СТОЛБЦОВ И ЗАПИСЬ В СПИСОК
    s2.append(sumColumn(matrix, o))
    o += 1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()


ds1 = np.trace(b)
b = np.fliplr(b)
ds2 = np.trace(b)

for i in range(len(s1)-1):
    if s1[i] == s1[i+1]:
        flag = 0
    else:
        flag = 1

if flag == 0:
    for i in range(len(s2) - 1):
        if s2[i] == s2[i + 1]:
            flag = 0
        else:
            flag = 1

if flag == 0:
    if ds1 == ds2:
        print("Квадрат магический")
    else:
            print("Квадрат не магический")
else:
    print("Квадрат не магический")




# print(s1)
# print(s2)
# print(ds1)
# print(ds2)