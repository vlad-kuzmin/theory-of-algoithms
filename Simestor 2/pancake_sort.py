import random
def pancake(data):
    if len(data) > 1:
        for size in range(len(data), 1, -1):
            # Позиция максимума в неотсортированной части
            maxindex = max(range(size), key = data.__getitem__)
            if maxindex + 1 != size:
                # Если максимум не слева, то нужно развернуть
                if maxindex != 0:
                    # Переворачиваем так, чтобы максимум оказался слева
                    data[:maxindex + 1] = reversed(data[:maxindex + 1])
                # Переворачиваем неотсортированную часть массива,
                # максимум становится на своё место
                data[:size] = reversed(data[:size])
                print(data)
                print(size, maxindex)
    return data


data = []
for i in range(0, 30):
    data.append(random.randint(0, 30))

print(data)
pancake(data)
