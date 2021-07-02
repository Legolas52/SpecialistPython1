# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination2(num_items, items_on_page):
    if num_items / items_on_page == int(num_items / items_on_page):
        return items_on_page
    return num_items % items_on_page


print(pagination2(5, 2))
print(pagination2(5, 1))
print(pagination2(26, 7))
print(pagination2(10, 2))
print(pagination2(6, 3))
print(pagination2(19, 3))
