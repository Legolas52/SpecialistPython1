# Напишите функцию находящую n-ое число Фибоначчи.
def numb_fib(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return numb_fib(n - 1) + numb_fib(n - 2)


print(numb_fib(10))
print(numb_fib(3))
print(numb_fib(5))
