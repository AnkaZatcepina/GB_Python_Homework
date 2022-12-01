#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def negafibonacci(n):
    result = [0,]
    for i in range(1,n+1):
        if i == 1:
            result.insert(0, 1) 
            result.append(1) 
        elif i == 2:
            result.insert(0, -1) 
            result.append(1) 
        else:
            result.insert(0, result[1] - result[0])
            length = len(result)                       
            result.append(result[length-2] + result[length-1]) 
    return result 

print(negafibonacci(8))               