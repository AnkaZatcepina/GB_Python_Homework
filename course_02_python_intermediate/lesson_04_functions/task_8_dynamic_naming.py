"""
    ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
    ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
    оканчивающихся на s (кроме переменной из одной буквы s) на None.
    ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""
LETTER = 's'

def replace_to_none() -> None:
    global_vars = globals()
    new_vars = {}
    for key, value in global_vars.items():
        if key == LETTER:
            continue
        if key.endswith(LETTER):
            new_vars[key[:-1]] = value
            global_vars[key] = None
    for key, value in new_vars.items():
        global_vars[key] = value      

s = 5
var_1s = 2 

replace_to_none()

print(s,var_1s,var_1)
