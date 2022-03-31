print("3-Х ЗНАЧНЫЕ ЧИСЛА КРАТНЫЕ 17:")
for i in range(100, 1000):
    nlist = list(list(str(i))) # В данной строчке мы делем число на отдельные цифры, помещаем их в список
    nlist = [int (x) for x in nlist]
    if sum(nlist) % 17 == 0:
        rlist = int(str(i)) # Тут обратно из списка делаем целое число и выводим
        print(rlist)