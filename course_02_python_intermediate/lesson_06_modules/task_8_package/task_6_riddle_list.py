"""
    Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). 
    Функция формирует словарь с информацией о результатах отгадывания. 
    Для хранения используйте защищённый словарь уровня модуля.
    Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. 
    Для формирования результатов используйте генераторное выражение.
"""

__all__ = ['riddle', 'riddle_quiz', 'show_statistic']

_data = {}

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
        result = riddle(riddle_text, answers, attempts)
        print(result) 
        add_statistic(riddle_text, result) 

def add_statistic(riddle_text: str, attempts: int): 
    _data.update({riddle_text:attempts})

def show_statistic(): 
    print('Статистика отгадывания:') 
    result = '\n'.join(f'Загадка "{riddle_text}" ' \
                        f'{f"угадана с {attempts} попытки" if attempts > 0 else "не угадана"}' \
                        for riddle_text, attempts in _data.items() )
    print(result)                    


if __name__ == '__main__':
    riddle_quiz()  
    show_statistic() 