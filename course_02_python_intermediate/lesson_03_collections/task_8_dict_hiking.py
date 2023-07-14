"""
    Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. 
    Ответьте на вопросы:
    ✔ Какие вещи взяли все три друга
    ✔ Какие вещи уникальны, есть только у одного друга
    ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
    ✔ Для решения используйте операции с множествами. 
    Код должен расширяться на любое большее количество друзей.
"""

dict_hiking = { 
    'Вова': ('спички', 'палатка', 'топор', 'нож', 'спальный мешок'),
    'Лена': ('спички', 'нож', 'аптечка', 'спальный мешок', 'еда'),
    'Дима': ('посуда', 'спальный мешок', 'еда', 'нож', 'веревка'),
    }

result = ''

for person, person_items in dict_hiking.items():
    everybody = set(person_items)
    unique    = set(person_items)
    friends_have = set()
    for friend, friend_items in dict_hiking.items():
        if friend == person:
            continue
        everybody = everybody & set(friend_items)
        unique -= set(friend_items) 
        if len(friends_have) == 0:
            friends_have = set(friend_items)
        else:
            friends_have = friends_have & set(friend_items)

    if len(unique) > 0:
        result += f'Только {person} взял: {unique}\n'    
    
    friends_have = friends_have - set(person_items)
    if len(friends_have) > 0:     
        result += f'Только {person} не взял: {friends_have}\n'     

result = f'Все взяли: {everybody}\n' + result
print(result)
   
