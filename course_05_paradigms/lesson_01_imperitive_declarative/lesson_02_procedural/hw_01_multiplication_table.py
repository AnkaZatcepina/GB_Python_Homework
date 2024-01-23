MIN_I = 1
MAX_I = 9
MIN_J = 1
MAX_J = 10
EQUALITY_LENGTH = 12

print('ТАБЛИЦА УМНОЖЕНИЯ')

for i in range(MIN_I,MAX_I+1):
    for j in range(MIN_J,MAX_J+1): 
        one_equality = f'{j} X {i} = {i*j}'
        one_equality = one_equality + ' '*(EQUALITY_LENGTH - len(one_equality))
        print(one_equality, end='')
    print()
