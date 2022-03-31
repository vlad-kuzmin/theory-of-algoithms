import random


def fill(value, n):
    mas = []
    for i in range(value):
        mas.append(random.randint(0, n))

    return mas


m = fill(20, 10)


def cnt_sort(mas):
    counted_mas = [0 for i in range(11)]
    sorted_mas = []

    for i in mas:
        counted_mas[i] += 1

    for i in range(11):
        for j in range(counted_mas[i]):
            sorted_mas.append(i)

    print("\033[37m {}".format(mas))
    print("\033[31m {}".format(counted_mas))
    print("\033[32m {}".format(sorted_mas))


cnt_sort(m)
