# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр", "Александр" , "Алексей", "Виктор"]

# TODO: your code here

length = 0
for name in names:
    if len(name) > length:
        length = len(name)

for name in names:
    if len(name) == length:
        print(name)
        length = 0
