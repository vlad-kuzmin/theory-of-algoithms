it = range(0, 1000000)  # Задаем диапазон строки от "000001" до "999999"
ls = list(map("{:06}".format, it[1:999999]))
lucky_ls = []  # Список счастливых билетов

for i in ls:  # Достаем из списка всех билетов от "000001" до "999999"
    if i[0] + i[1] + i[2] == i[3] + i[4] + i[5]:  # Сравыниваем левую и правую сторону (I+ J + K = L + M + N)
        lucky_ls.append(i)  # Если True то добавляем билет в список lucky_ls

print("Число счастливых билетов, номера которых меняются от 000001 до 999999:",
      len(lucky_ls) + 1)  # Вывод количества элементов в списке счастливых билетов
