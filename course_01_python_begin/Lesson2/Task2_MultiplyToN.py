#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите положительное целое число N:')) 

listMult = []
multipl = 1
listMult.append(multipl)
for i in range(2,n+1):
    multipl *= i
    listMult.append(multipl)
print(f'Список произведение чисел от 1 до N = {listMult}')      