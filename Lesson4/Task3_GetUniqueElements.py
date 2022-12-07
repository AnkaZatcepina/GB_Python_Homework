#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def getUniqueElements(lst):
    newLst = []
    st = set(lst)
    for i in st:
        if lst.count(i) == 1:
            newLst.append(i)
    return newLst  
    
print(getUniqueElements([1,1,2,4,5,6,7,7,8])) 