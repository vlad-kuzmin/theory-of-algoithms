import random
n = int(input("Введите длинну массива: "))
mas = list()
ind5 = list()


for i in range(n):  # Заполняем массив рандомными числами
    mas.append(random.randint(10, 100))


for i in mas:
    i = str(i)
    if i[len(i)-1] == "5":  # Проверяем закнчивается ли элемент числом 5
        ind5.append(mas.index(int(i)))   # Добавление индексов этих элементов в массив ind56


print(mas)
print("Номера элементов массива заканчивающихся цифрой 5:", *ind5)