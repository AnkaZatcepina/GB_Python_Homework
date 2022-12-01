#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def multiplyListPairs(intList):
    length = len(intList)
    multList = []
    for index, value in enumerate(intList):
        #Выходим из цикла, если прошли середину списка
        if index >= length / 2:
            break 
        multList.append(value * intList[length - index - 1])
    return multList

list = [2, 3, 4, 5, 6]
print(multiplyListPairs(list)) 
list2 = [2, 3, 5, 6]
print(multiplyListPairs(list2))     