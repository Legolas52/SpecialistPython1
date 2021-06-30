# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

n = 20
summ = 0
numbers = []
for i in range(20):
    numbers.append(random.randint(-100, 100))

for numb in numbers:
    if numb > 0 and numb % 2 == 0:
        summ += numb

print(numbers)
print(f" Сумма равна {summ}")
