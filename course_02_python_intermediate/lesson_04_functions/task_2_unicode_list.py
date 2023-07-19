"""
    ✔ Напишите функцию, которая принимает строку текста.
    ✔ Сформируйте список с уникальными кодами Unicode каждого
    символа введённой строки отсортированный по убыванию.
"""

def create_unicode_list(inp_str: str) -> [int]:
    uni_set = set(map(ord, inp_str))
    uni_sorted = sorted(list(uni_set),reverse=True)
    return uni_sorted 

print(create_unicode_list('abce'))      