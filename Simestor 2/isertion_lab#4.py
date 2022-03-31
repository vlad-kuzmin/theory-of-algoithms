import random

m = []


def fill(mas, value):
    for i in range(value):
        mas.append(random.randint(0, value))

    return mas


print(fill(m, 20))


def sorting(mas):
    for i in range(0, len(mas)):
        temp = mas[i]
        j = i - 1

        while j >= 0 and temp < mas[j]:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = temp

    return mas


print(sorting(m))