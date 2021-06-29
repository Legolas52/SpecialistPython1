# По данному натуральному n выведите лесенку из n ступенек, i-я ступень состоит из чисел от 1 до i без пробелов.
# Формат входных данных: Вводится натуральное число n.
# Формат выходных данных: Выведите ответ на задачу.
# Пример:
# Для n = 4
# Нужно вывести:
# 1
# 12
# 123
# 1234

# TODO: your code here

number = int(input("Введи число: "))
variable = 0
new_number = 0
while variable < number:
    new_number = new_number * 10 + 1 + variable
    print(new_number)
    variable += 1
