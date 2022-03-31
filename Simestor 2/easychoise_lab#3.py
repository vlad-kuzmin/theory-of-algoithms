import random

m = []


def fill(mas, value):
    for i in range(value):
        mas.append(random.randint(0, value))

    return mas


print(fill(m, 20))


def sorting(mas):

    for i in range(0, len(mas) - 1):
        smallest = i
        for j in range(i + 1, len(mas)):
            if mas[j] < mas[smallest]:
                smallest = j
        mas[i], mas[smallest] = mas[smallest], mas[i]

    return mas


print(sorting(m))
