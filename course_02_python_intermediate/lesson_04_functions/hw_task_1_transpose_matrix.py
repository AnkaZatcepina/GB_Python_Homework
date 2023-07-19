# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix: [[]]) -> bool:
    length = len(matrix)
    for i in matrix:
        if len(i) != length:
            return False           
    for i in range(0,length):
        for j in range(i+1,length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]   
    return True         

matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix_1 if transpose_matrix(matrix_1) else 'Нельзя транспонировать')
matrix_2 = [[1,2,3],[4,5,6],[7,8,9,10]]
print(matrix_2 if transpose_matrix(matrix_2) else 'Нельзя транспонировать')
matrix_3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(matrix_3 if transpose_matrix(matrix_3) else 'Нельзя транспонировать')
