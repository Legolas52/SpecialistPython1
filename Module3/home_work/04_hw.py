# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random

numbers = [-1, 10, 25, -9, 64, -81, 121, 81, 100, 76, -67, 225, -623, 625, 100, -91, 169]
sqrt_numbers = []

for numb in numbers:
    if numb > 0:
        if round(numb ** 0.5) == numb ** 0.5:
            sqrt_numbers.append(int(numb ** 0.5))

print(sqrt_numbers)
