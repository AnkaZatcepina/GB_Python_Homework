# Нарисовать в консоли ёлку, спросив у пользователя количество рядов.
MAX_ROW = 20
row_amount = int(input('Введите количество рядов для ёлки:')) 
if row_amount > MAX_ROW:
    print('Слишком много рядов, не получится нарисовать такую большую ёлку')
    exit()
for i in range(1,row_amount+1):
    print(' '*(row_amount - i) + '*'*(i*2-1))
