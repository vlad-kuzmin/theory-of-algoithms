import random
import numpy as np

mas4 = [[],
        [],
        [],
        []]


for i in range(len(mas4)):
    for j in range(4):  # Заполняем массив рандомными числами
        mas4[i].append(random.randint(10, 100))


def convert_to(mas):
    con_mas = []
    for l in mas:
        for r in l:
            con_mas.append(r)
    return con_mas


B = convert_to(mas4)


def sorting(B):
    for i in range(1, len(B) - 1):
        for j in range(len(B) - i):
            if B[j] > B[j + 1]:
                x = B[j]
                B[j] = B[j + 1]
                B[j + 1] = x
    return B


def convert_to_mas4(mas):
    a = np.array(mas)
    b = a.reshape(-1, 4)
    return b


def m_print(mas):
    for i in mas:
        print(i)


m_print(mas4)
print()

cn_mas = convert_to(mas4)
print(cn_mas)
print()

srt_mas = sorting(cn_mas)
print(srt_mas)
print()

srt_mas4 = convert_to_mas4(srt_mas)
m_print(srt_mas4)
