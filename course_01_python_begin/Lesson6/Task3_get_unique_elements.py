#Предложить улучшения кода для уже решённых задач:
#С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def get_unique_elements(lst):
    return list(filter(lambda i: (lst.count(i) == 1), lst))  
    
print(get_unique_elements([1,1,2,4,5,6,7,7,8])) 