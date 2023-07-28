"""
    ✔ Напишите функцию, которая генерирует
    псевдоимена.
    ✔ Имя должно начинаться с заглавной буквы,
    состоять из 4-7 букв, среди которых
    обязательно должны быть гласные.
    ✔ Полученные имена сохраните в файл.
"""
__all__ = ['append_file_pseudonames', 'generate_name', 'validate_name']

import random

MIN_INT: int = -1000
MAX_INT: int = 1000

def generate_name() -> str:
    VOVELS = 'аааааееееёиииииоооооооууэюя'
    CONSONANTS = 'ббвввггдджжзйккккллмммнннппппрррррссссстттттфхцчшщ'
    def generate_syllable(letters):
        return ''.join((random.choice(VOVELS if letter == '0' else CONSONANTS) for letter in letters))

    syll_types = ['0', '0', '01', '01', '10', '10', '10', '101', '1011']
    syllables = [generate_syllable(syll_type) for syll_type in syll_types] 

    return ''.join(random.sample(syllables, 3))   

def validate_name():
    while True:
        name = generate_name()
        if 4<=len(name)<=7:
            break
    return name.capitalize()

def append_file_pseudonames(filename: str = 'task_2_file.txt', limit: int = 3):
    with open(filename, mode='a', encoding='utf-8') as file:
        for _ in range(limit):
            file.write(validate_name() + '\n')        

if __name__ == '__main__':
    append_file_pseudonames()
