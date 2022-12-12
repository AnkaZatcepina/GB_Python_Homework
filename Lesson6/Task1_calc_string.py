#Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
def calc_string(string):
    result = 0
    print(string)

    num = string.split()
    while len(num) > 1:
        while '*' in num or '/' in num :
            if num.count('*') > 0 and num.count('/') > 0:
                if num.index('/') > num.index('*'):
                    num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                    num.pop(num.index('*') + 1)
                    num.pop(num.index('*'))
                else:
                    num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                    num.pop(num.index('/') + 1)
                    num.pop(num.index('/'))
            else:
                if '*' in num:
                    num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                    num.pop(num.index('*') + 1)
                    num.pop(num.index('*'))
                else:
                    num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                    num.pop(num.index('/') + 1)
                    num.pop(num.index('/'))
        while '+' in num or '-' in num :
            if num.count('+') > 0 and num.count('-') > 0:
                if num.index('-') > num.index('+'):
                    num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                    num.pop(num.index('+') + 1)
                    num.pop(num.index('+'))
                else:
                    num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                    num.pop(num.index('-') + 1)
                    num.pop(num.index('-'))
            else:
                if '+' in num:
                    num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                    num.pop(num.index('+') + 1)
                    num.pop(num.index('+'))
                else:
                    num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                    num.pop(num.index('-') + 1)
                    num.pop(num.index('-'))  
    return num[0]

print(calc_string('1 + 2 * 3'))  
print(calc_string('1 - 2 * 3'))  
print(calc_string('4 / 2 * 2'))  
print(calc_string('4 + 5 * 3 - 3 * 2'))  


