# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# #
from coordinate_geometry.point import *

x1 = float(input("введите координату X первой точки: "))
y1 = float(input("введите координату Y первой точки: "))
x2 = float(input("введите координату X второй точки: "))
y2 = float(input("введите координату Y второй точки: "))
# #
# # length = ((x1-x2)**2+(y1-y2)**2)**0.5
# #
# # print(f"A ({x1},{y1}); B ({x2},{y2}) -> {length}")


p1=point(x1,y1)
p2=point(x2,y2)
print(p1.distance(p2))