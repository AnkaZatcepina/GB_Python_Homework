"""
Нормализация данных

Реализовать с использованием функциональной парадигмы процедуру normalization, которая выполняет
нормализацию полученного массива по приведенной формуле нормализованного значения элемента, где
    ○ x_norm - нормализованное значение элемента
    ○ x - исходное значение элемента
    ○ x_max, x_min - максимальное и минимальное значение в массиве
   
"""

def normalize(data):
    min_val = min(data)
    max_val = max(data)

    def normalize_element(x):
        return (x - min_val) / (max_val - min_val)

    return list(map(normalize_element, data)) 

data = [i for i in range(50,150)]

print(normalize(data))