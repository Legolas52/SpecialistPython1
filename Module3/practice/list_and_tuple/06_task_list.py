# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("first: "))  # Первое число
second_number = int(input("second: "))  # Второе число

a = max(first_number, second_number)
b = min(first_number, second_number)
my_numbers = []

for numb in range(b, a):
    if numb % 3 == 0:
        my_numbers.append(numb)
print(my_numbers)
