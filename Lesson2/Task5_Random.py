#Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом)
#Взяла целые числа от 0 до n
from datetime import datetime

def myRandom(n):
    myRandom = (43 * float(datetime.now().time().microsecond) - float(datetime.now().time().second)) ** n % (n+1)
    return abs(int(myRandom))

print(myRandom(1)) 
print(myRandom(1))
print(myRandom(1))   
print(myRandom(34))    
print(myRandom(34))      