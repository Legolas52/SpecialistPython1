# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
numbers = [5, 1, -3, 6, 7, 8, -8, -9, 4]
summ = 0
for number in numbers:
    summ += number
print("сумма=", summ)
