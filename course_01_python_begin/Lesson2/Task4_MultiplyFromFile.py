#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Введите положительное целое число N:')) 

#Заполнение списка
listValues = []
for i in range(n*2 + 1):
    listValues.append(-n + i)
print(listValues)

#Чтение позиций из файла
multiply = 1
with open("file.txt",'r') as data_file:
    for line in data_file:
        try:
            index = int(line)
            multiply *= listValues[index]
        except:
            pass
print(f'Произведение существующих значений = {multiply}')        

