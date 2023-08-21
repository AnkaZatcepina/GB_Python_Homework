"""
    Создайте функцию, которая запрашивает числовые данные от
    пользователя до тех пор, пока он не введёт целое или
    вещественное число.
    Обрабатывайте не числовые данные как исключения.
"""

def get_input() -> int | float:
    while True:
        value = input('Введите целое или вещественное число: ')
        try:
            result = int(value)
            break
        except ValueError as e:
            print(f'{value} не удалось привести к целому числу')
            try:
                result = float(value)
                break
            except ValueError as e:
                print(f'{value} не удалось привести к вещественному числу')
    return result

if __name__ == '__main__':
    print(get_input())    