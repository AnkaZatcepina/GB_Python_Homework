"""
    Дан список целых чисел numbers. Необходимо написать в императивном и декларативном стилях процедуру для
    сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
"""

def sort_list_imperative(numbers):
    n = len(numbers)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j + 1]:
                swapped = True
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
         
        if not swapped:
            return numbers

def sort_list_declarative(numbers):
    return numbers.sort(reverse=True)

if __name__ == '__main__':
    numbers_1 = [2,7,6,1,3]
    numbers_2 = [1,4,7,2,8]
    sort_list_imperative(numbers_1)
    print(numbers_1)
    sort_list_declarative(numbers_2)
    print(numbers_2)
