#Бинарный поиск

def binary_search(list, left, right, value):
    if (right < left):
        return None
    else:
        mid = left + ((right - left) // 2)
        if list[mid] > value:
            return binary_search(list, left, mid-1,value)
        elif list[mid] < value:
            return binary_search(list, mid+1, right, value)
        else:
            return mid

list = [8,11,24,56,88,131]
print(binary_search(list, 0, 5, 24))
print(binary_search(list, 0, 5, 51))