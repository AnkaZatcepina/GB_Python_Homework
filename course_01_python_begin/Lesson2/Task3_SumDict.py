#Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

def sumDict(n):
    sum = 0
    dictionary = {}
    for i in range(1,n+1):
        dictionary[i] = (1 + (1/i))**i  
        sum += dictionary[i]
    print(dictionary) 

    return sum

print(sumDict(1))    
print(sumDict(3)) 