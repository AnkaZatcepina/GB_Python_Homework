"""
Создайте программу для игры с конфетами человек против бота.

Условие задачи: На столе лежит 2021 конфета. Вы играете с ботом, делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 

Подумайте как наделить бота ""интеллектом""
"""
import random
import os
import time

MIN_AMOUNT = 1
MAX_AMOUNT = 28

quantity_on_table = 100
first_player_turn = True
winner = ''

#Проверка, кончилась ли игра
def check_winner():
    return quantity_on_table == 0

#Проверка количества взятых конфет
def check_amount(amount):
    global quantity_on_table
    if not amount.isnumeric():
        print("Это не число!")
        return False
    if not (MIN_AMOUNT <= int(amount) <= MAX_AMOUNT):
        print(f"За ход можно брать от {MIN_AMOUNT} до {MAX_AMOUNT} конфет")
        return False
    if int(amount) > quantity_on_table:
        print("На столе нет столько конфет!" ) 
        return False
    return True     
            
#Умный ход бота
def bot_smart_take():
    #Забираем всё, если конфет мало
    if quantity_on_table <= MAX_AMOUNT:
        return quantity_on_table
    #Берём такое количество, чтоб оставалось число кратное MAX_AMOUNT+1 
    return quantity_on_table - (quantity_on_table // (MAX_AMOUNT+1) * (MAX_AMOUNT+1)) 

#Xод игрока. возвращает количество конфет
def player_turn():
    global first_player_turn, quantity_on_table, name1, name2

    print()
    print(f"На столе есть {quantity_on_table} конфет.")

    name = name1 if first_player_turn else name2
    print(f"Ходит игрок {name}") 

    #Ход игрока
    if first_player_turn: 
        while True:
            take_amount = input(f"{name}, введите количество конфет: ")
            if check_amount(take_amount):
                break
    #Ход бота
    else:
       while True:
            time.sleep(1)
            take_amount = str(bot_smart_take())
            print(f"{name} взял конфет: {take_amount}")
            time.sleep(1)
            if check_amount(take_amount):
                break            

    quantity_on_table -= int(take_amount)
    first_player_turn = not first_player_turn  

    if check_winner():
        return name
    return ""    
    
#Очистка консоли
os.system('clear')

#Приветственное слово, регистация
print("Добрый день! Это игра с конфетами для 2х игроков")
print("Кто заберёт последнюю конфету со стола - победитель")
print(f"За ход можно брать от {MIN_AMOUNT} до {MAX_AMOUNT} конфет")
name1 = input("Введите Ваше имя: ")
name2 = "Бот"

#Определение первого игрока
first_player_turn = bool(random.getrandbits(1))

#Ходы игроков
while winner == "":
    winner = player_turn()

#Конец игры 
print()   
print(f"Выиграл игрок {winner}")    