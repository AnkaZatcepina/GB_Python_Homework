#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

def getDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

print(getDistance(3,6,2,1))  
print(getDistance(7,-5,1,-1))
 