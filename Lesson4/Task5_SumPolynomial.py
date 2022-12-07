#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
def getList(poly):
    lst = poly[:-4].replace(' ', '').replace('-', '+-').split('+')
    if '' in lst: lst.remove('')
    return lst
    
def getDegree(s):
    if s.find('^') >= 0:   
        degree = s[s.find('^')+1:len(s)]
    elif s.find('x') >= 0: 
        degree = 1 
    else: degree = 0               
    return int(degree)
    
def getCoeff(s): 
    if s.find('*') >= 0:   
        coeff = s[0:s.find('*')]
    elif s.find('x') >= 0:
        if s.find('-') >= 0:
            coeff = -1
        else: coeff = 1 
    else:
        coeff = s    
    return int(coeff)    

def sumPolynomial(poly1, poly2):
    s = ''
    lst1 = getList(poly1)
    lst2 = getList(poly2)
    degree1 = getDegree(lst1[0])
    degree2 = getDegree(lst2[0]) 
    if degree2 > degree1:
        lst1, lst2 = lst2, lst1
    while len(lst1) or len(lst2) > 0:
        if len(lst1) > 0:
            degree1 = getDegree(lst1[0])
            coeff1 = getCoeff(lst1[0])
        else:
            degree1 = -1
            coeff1 = 0
        if len(lst2) > 0:
            degree2 = getDegree(lst2[0])
            coeff2 = getCoeff(lst2[0])
        else:
            degree2 = -1
            coeff2 = 0
        if degree1 == degree2:
            s += f' + {coeff1 + coeff2}*x^{degree1}'
            lst1.pop(0)
            lst2.pop(0)
        elif degree1 > degree2: 
            s += f' + {coeff1}*x^{degree1}'
            lst1.pop(0)
        else:
            s += f' + {coeff2}*x^{degree2}'
            lst2.pop(0)
 
    s = s[2 : len(s)] + ' = 0'  
    s = s.replace('+ -', '- ') 
    s = s.replace(' 1*', ' ')  
    s = s.replace('-1*', '-')   
    s = s.replace('x^1', 'x')      
    s = s.replace('*x^0', '')      
    s = s.replace('x^0', '')  
    return s

with open('polynomial.txt', 'r') as f:
    s1 = f.readline()
    print(s1)
with open('polynomial2.txt', 'r') as f:
    s2 = f.readline()
    print(s2)
summa = sumPolynomial(s1,s2)
print(summa)
with open('polynomial_sum.txt', 'w') as f:
   f.write(summa)