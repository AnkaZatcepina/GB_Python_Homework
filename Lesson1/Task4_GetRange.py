#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
quater = int(input('Введите четверть:')) 
if quater == 1:
    print('x >= 0, y >= 0')
elif quater == 2:
    print('x < 0, y >= 0')
elif quater == 3:
    print('x < 0, y < 0')       
elif quater == 4:
    print('x >= 0, y < 0')   
else:
    print('Некорректный ввод') 