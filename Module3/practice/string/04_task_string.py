# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here

text = input("text: ")
count1 = text.count(" ")
text = text.split()

i = 0
j = 0
while i <= count1:
    if len(text[i]) > 5:
        j +=1
    i += 1
print(j)
