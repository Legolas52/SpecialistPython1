# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    return (x-xc)**2+(y-yc)**2 < r**2


print(point_in_circle(5,6,1,2,10))
print(point_in_circle(10,20,1,1,5))
print(point_in_circle(0,0,1,1,10))
