print("ВВЕДИТЕ 2 ЧЕТЫРЕХЗНАЧНЫХ ЧИСЛА", "\n")
n = int(input("Введите первое число: "))
if n > 999:
    print()
else:
    print("ERROR: ЧИСЛО НЕ ЧЕТЫРЕХЗНАЧНОЕ. ПОВТОРИТ ПОПЫТКУ")

s = int(input("Введите второе число: "))
if s > 999:
    print()
else:
    print("ERROR: ЧИСЛО НЕ ЧЕТЫРЕХЗНАЧНОЕ. ПОВТОРИТ ПОПЫТКУ")


for i in range(n, s):
    nlist = list(str(i))  # В данной строчке мы делем число на отдельные цифры
    c = 0
    v = len(nlist)
    p = nlist.count(nlist[2])

    if p == 3:
        print(i)
