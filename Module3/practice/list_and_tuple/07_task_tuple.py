# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

n = tup[0]
for numb in tup:
    n = max(n, numb)

print("max=", n)

# TODO: your code here
