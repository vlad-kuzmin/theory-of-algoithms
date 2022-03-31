import random


def fill(m, n, rnd):
    mas_ = [[] for i in range(m)]

    for i in range(len(mas_)):
        for j in range(n):
            mas_[i].append(random.randint(0, rnd))

    return mas_


mas = fill(3, 3, 20)

print("Изначальный массив")


def mprint(mas_):
    for i in mas_:
        print(i)


mprint(mas)


def diagonal(mas_):
    dgl_ = []

    for i in range(len(mas_)):
        dgl_.append(mas_[i][i])

    return dgl_


print()

dgl = diagonal(mas)

print(f'{dgl} - главная диагональ')

print()


def sorting(mas_):
    for i in range(0, len(mas_)):
        temp = mas_[i]
        j = i - 1

        while j >= 0 and temp < mas_[j]:
            mas_[j + 1] = mas_[j]
            j -= 1
        mas_[j + 1] = temp

    return mas_


def insertion(mas_, dgl_):
    for i in range(len(mas_)):
        mas_[i][i] = dgl_[i]

    return mas_


print("Отсортированный массив")
mprint(insertion(mas, sorting(dgl)))
