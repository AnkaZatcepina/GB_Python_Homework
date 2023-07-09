""" 
    Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
    Дано a, b, c - стороны предполагаемого треугольника. 
    Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
    Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
    Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""
side_a = int(input('Введите сторону a: ')) 
side_b = int(input('Введите сторону b: ')) 
side_c = int(input('Введите сторону c: ')) 

if (   (side_a+side_b) < side_c
    or (side_b+side_c) < side_a
    or (side_c+side_a) < side_b):
    print('Треугольника с такими сторонами не существует')
    exit()

if side_a == side_b == side_c:
    print('Это равносторонний треугольник')
    exit()   

if side_a == side_b or side_b == side_c or side_c == side_a:
    print('Это равнобедренный треугольник')
    exit()  

print('Это разносторонний треугольник')         
