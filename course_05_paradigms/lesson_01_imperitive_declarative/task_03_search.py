def search_imperitive(array, target):
    for num in array:
        if num == target:
            return True
    return False

def search_declarative(array, target):
    return target in array  