"""
    ✔ Функция получает на вход список чисел.
    ✔ Отсортируйте его элементы in place без использования
    встроенных в язык сортировок.
    ✔ Как вариант напишите сортировку пузырьком.
    Её описание есть в википедии.
"""

def sort_digits(arr: [int]):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


arr = [4,5,2,7,5,10]   
sort_digits(arr)  
print(arr)       