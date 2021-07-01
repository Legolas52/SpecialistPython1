# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    new_number = number
    temp = 0
    while new_number > 0:
        digit = new_number % 10
        new_number = new_number // 10
        temp = temp * 10 + digit

    return temp == number

i=0
a=52
b=10000
for number in range(a,b):
    if palindrome(number):
        i+=1

print(i)
