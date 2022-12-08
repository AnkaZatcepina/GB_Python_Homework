#Создайте программу для игры в ""Крестики-нолики"".
import random
import os

BOARD_LENGTH = 3
EMPTY_CELL = "-"
CROSS = "X"
ZERO = "0"
BOARD_NUMBERS = [[*range(1,4)],[*range(4,7)],[*range(7,10)]]


first_player_turn = True
winner = ''
current_player_sign = ""

#Объявляем поле из пустых клеток
board = []
for i in range(BOARD_LENGTH):
    column = []
    for j in range(BOARD_LENGTH):
        column.append('-')
    board.append(column)
#board = [['-']*BOARD_LENGTH]*BOARD_LENGTH

#Вывод доски
def print_board(board):
    for i in range(BOARD_LENGTH):
        for j in range(BOARD_LENGTH):
            print(board[i][j], end = " ")
        #Переход на новую строку
        print()
    print()  

#Проверка, кончилась ли игра
def check_winner():
    global board, current_player_sign
    win = False

    #Проверка рядов
    for i in range(BOARD_LENGTH):
        win = True
        for j in range(BOARD_LENGTH):
            if board[i][j] != current_player_sign:
               win = False 
               break
        if win: return win    
    

    #Проверка столбцов
    for j in range(BOARD_LENGTH):
        win = True
        for i in range(BOARD_LENGTH):
            if board[i][j] != current_player_sign:
               win = False
               break
        if win: return win    

    #Проверка диагоналей
    win = True
    for i in range(BOARD_LENGTH):
        if board[i][i] != current_player_sign:
            win = False 
    if win: return win

    win = True
    for i in range(BOARD_LENGTH):
        if board[BOARD_LENGTH - i - 1][i] != current_player_sign:
            win = False 

    return win 

#Проверка на ничью
def check_draw():                                     
    for i in range(BOARD_LENGTH):
        for j in range(BOARD_LENGTH):
            if board[i][j] == EMPTY_CELL:
               return False 
    return True           

#Проверка клетки
def check_cell(cell_number):
    if not cell_number.isnumeric():
        print("Некорректно введена цифра клетки, введите число от 1 до 9")
        return False
    if not (1 <= int(cell_number) <= 9):
        print("Некорректно введена цифра клетки, введите число от 1 до 9")
        return False
    if board[get_cell(cell_number)[0]][get_cell(cell_number)[1]] != EMPTY_CELL:
        print("Клетка уже занята!" ) 
        return False
    return True

#Строка и столбец по номеру клетки
def get_cell(cell_number):
    cell = ((int(cell_number) - 1) // 3, (int(cell_number) - 1) % 3 )
    return cell        

#Xод игрока. возвращает количество конфет
def player_turn():
    global board, first_player_turn, current_player_sign

    print_board(board)
    
    name = name1 if first_player_turn else name2
    print(f"Ходит игрок {name}, {current_player_sign}")  
    while True:
        cell_number = input(f"{name}, введите номер клетки: ")
        if check_cell(cell_number):
            break

    cell =  get_cell(cell_number)         
    board[cell[0]][cell[1]] = current_player_sign         
    first_player_turn = not first_player_turn  

    if check_winner():
        return name

    if check_draw():   
        return 'Ничья'

    if current_player_sign == CROSS:
        current_player_sign = ZERO 
    else:
        current_player_sign = CROSS 

    return ""    
    
#Очистка консоли
os.system('clear')      

#Приветственное слово, регистация
print("Добрый день! Это игра крестики-нолики")
name1 = input("Введите имя 1го игрока: ")
name2 = input("Введите имя 2го игрока: ")
print("Клетки нумеруются слева направо, сверху вниз")
print("Для хода нужно ввести номер клетки")

print_board(BOARD_NUMBERS)
print("Сейчас доска пустая")

#Определение первого игрока
first_player_turn = bool(random.getrandbits(1))
current_player_sign = CROSS 

#Ходы игроков
while winner == "":
    winner = player_turn()

#Конец игры 
print() 
if winner == "Ничья":
    print("Ничья!")
else:    
    print(f"Выиграл игрок {winner}") 
print_board(board) 
   

