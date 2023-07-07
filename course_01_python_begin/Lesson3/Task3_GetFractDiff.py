#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
def getFractDiff(floatList):
    fractList = [x % 1 for x in floatList]
    diff = max(fractList) - min(fractList)
    return diff

floatList = [1.1, 1.2, 3.1, 5.1, 10.01]
print(getFractDiff(floatList))