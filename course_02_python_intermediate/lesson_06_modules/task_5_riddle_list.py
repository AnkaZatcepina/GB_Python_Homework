"""
    Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
    Ключ словаря - загадка, значение - список с отгадками. 
    Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки. 
"""

def riddle(text: str, answers: [str], attempts: int)->int:
    print(text)
    for i in range(1, attempts+1):
        answer = input(f'Введите ответ: ')
        if answer in answers:
            print('Верно!')
            return i
        else:
            print('Не верно!') 
    print('Количество попыток закончилось!')       
    return 0

def riddle_quiz(attempts: int = 3):
    riddle_dict = {
        'Зимой и летом одним цветом': ['ёлка','елка','ёлочка','елочка'],
        'Висит груша нельзя скушать': ['лампочка',],
        'Сидит дед, во 100 шуб одет': ['лук','луковица'],
        } 
    for riddle_text, answers in riddle_dict.items():
        print(riddle(riddle_text, answers, attempts))      

if __name__ == '__main__':
    riddle_quiz()   