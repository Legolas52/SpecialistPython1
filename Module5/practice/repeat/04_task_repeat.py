# Напишите функцию принимающую общее количество объектов(например, товаров)
# которые нужно отобразить и количество объектов, которые нужно отобразить на каждой странице.
# Функция должна вычислять количество страниц для отображения всех объектов.

# Под пагинацией понимают показ ограниченной части информации на одной
# веб-странице и вывода списка остальных страниц.

def pagination(num_items, items_on_page):
    if num_items / items_on_page == int(num_items / items_on_page):
        return num_items // items_on_page
    return num_items // items_on_page + 1


print(pagination(5, 2))
print(pagination(5, 1))
print(pagination(26, 7))
print(pagination(10, 2))
print(pagination(6, 3))
print(pagination(19, 3))

