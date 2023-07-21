"""
    ✔ Выведите в консоль таблицу умножения
    от 2х2 до 9х10 как на школьной тетрадке.
    ✔ Таблицу создайте в виде однострочного
    генератора, где каждый элемент генератора —
    отдельный пример таблицы умножения.
    ✔ Для вывода результата используйте «принт»
    без перехода на новую строку.
"""

MIN_I = 2
MAX_I = 9
MIN_J = 2
MAX_J = 10
EQUALITY_LENGTH = 12
COLUM_AMOUNT = 4

print('ТАБЛИЦА УМНОЖЕНИЯ')

for i in range(MIN_I,MAX_I+1,4):
    for j in range(MIN_J,MAX_J+1): 
        for k in range(i, i + COLUM_AMOUNT):
            if k != i + COLUM_AMOUNT - 1:
                print(f'{k:>2} X {j:>2} = {k*j:>2}\t', end='')
            elif j != MAX_J:
                print(f'{k:>2} X {j:>2} = {k*j:>2}')
            else:
                print(f'{k:>2} X {j:>2} = {k*j:>2}')
                print()

mult_gen = (f'\t{k:>2} X {j:>2} = {k*j:>2}' if k != i + COLUM_AMOUNT - 1 else \
            f'\t{k:>2} X {j:>2} = {k*j:>2}\n' if j != MAX_J else \
            f'\t{k:>2} X {j:>2} = {k*j:>2}\n\n' \
            for i in range(MIN_I,MAX_I+1,4)
            for j in range(MIN_J,MAX_J+1)
            for k in range(i, i + COLUM_AMOUNT))  


print(*mult_gen)
