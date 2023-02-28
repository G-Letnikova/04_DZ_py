# Задача 24: про чернику, грядку, урожайность кустов и сбор ягод с трех соседних кустов

import random

n = int(input('введите число кустов на грядке: '))
series = [random.randint(1, 20) for _ in range(n)]  # урожайность каждого куста
print(series)

if n <= 3:  # кустов в грядке мало
    print(sum(series))
else:
    series = series + series[:2]  # первые два куста дописываем в конец
    i = 0
    max_berry = sum(series[i:i + 3])  # максимальный урожай с трех соседних кустов = 1му срезу

    while i < len(series) - 2:  # проходимся срезами по 3
        if max_berry < sum(series[i:i + 3]):
            max_berry = sum(series[i:i + 3])
        i += 1

    print(max_berry)
