# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import math
print('Введите координаты первой точки')
xA = int(input('X: '))
yA = int(input('Y: '))

print('Введите координаты второй точки')
xB = int(input('X: '))
yB = int(input('Y: '))
dis = math.sqrt((xB-xA)**2+(yB-yA)**2)
print("расстояние между заданными точками равно", dis)
