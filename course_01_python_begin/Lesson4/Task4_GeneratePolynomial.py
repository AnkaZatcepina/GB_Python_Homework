#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)* многочлена и записать в файл многочлен степени k.   
import random

def generatePolynomial(k,maxCoeff):
    s = ''
    for i in range(0,k+1):
        #Генерируем коэффициент
        coeff = random.randint(-maxCoeff, maxCoeff)
        print(coeff)
        #Выводим только ненулевые элементы
        if coeff !=0:
            strCoeff = f'+ {coeff}*'
            s += f'{strCoeff}x^{k-i} '
 
    s = s[1:] + '= 0'    
    s = s.replace('+ -', '- ') 
    s = s.replace('* ', ' ') 
    s = s.replace('*x^0', '')
    s = s.replace('^1', '')
    s = s.replace(' 1*x', ' x')
    s = s.replace('-1*x', '-x')
    
    print(s)            
    return s


with open('polynomial.txt', 'w') as f:
   f.write(generatePolynomial(3,100))
with open('polynomial2.txt', 'w') as f:
   f.write(generatePolynomial(5,2))   