"""
Создайте класс Матрица. Добавьте методы для:
    ○ вывода на печать,
    ○ сравнения,
    ○ сложения,
    ○ *умножения матриц
"""

class Matrix:
    """
    Operations with Matrixes: comparing, addition, multiplication
    """
    def __init__(self, matrix: []):
        self._matrix = matrix

    def check_dimensions(self,other): 
        if len(self._matrix) != len(other._matrix):
            raise RuntimeError("Matrixes have different dimensions") 
        for i,line in enumerate(self._matrix):
            if len(line) != len(other._matrix[i]):
                raise RuntimeError("Matrixes have different dimensions")   

    def __add__(self,other):
        self.check_dimensions(other)
        summa = []
        for i,line in enumerate(self._matrix):
            summa.append([])
            for j,item in enumerate(self._matrix[i]):
                summa[i].append(item + other._matrix[i][j])
        matrix = Matrix(summa)        
        return matrix

    def __mul__(self,other):
        rows = len(self._matrix)
        columns = len(self._matrix[0])
        if columns != len(other._matrix):
            raise RuntimeError("Columns amount of Matrix 1 must be equal to Rows amount of Matrix 2") 
        mult = [[0 for j in range(rows)] for i in range(rows)]
        
        for i in range(rows):
            for j in range(rows):
                for j1 in range(columns):
                    mult[i][j] += self._matrix[i][j1] * other._matrix[j1][j]
                
        matrix = Matrix(mult)        
        return matrix    

    def __eq__(self,other):
        self.check_dimensions(other)
        return self._matrix == other._matrix

    def __gt__(self,other):
        self.check_dimensions(other)
        for i,line in enumerate(self._matrix):
            for j,item in enumerate(self._matrix[i]):
                if item <= other._matrix[i][j]:
                    return False
        return True            

    def __ge__(self,other):
        self.check_dimensions(other)
        for i,line in enumerate(self._matrix):
            for j,item in enumerate(self._matrix[i]):
                if item < other._matrix[i][j]:
                    return False
        return True 

    def __str__(self):
        new_line = '\n'
        tab = '\t'
        result = f'[{new_line}' \
            f'{new_line.join((tab+str(line)) for line in self._matrix)}'\
            f'{new_line}]'    
        return result 

if __name__ == '__main__':
    matrix_1 = Matrix([
        [1,2,3,4],
        [5,6,7,8]
        ])  
    matrix_2 = Matrix([
        [1,2,3,4],
        [5,6,7,8]
        ])  
    matrix_3 = Matrix([
        [1,3,3,4],
        [5,6,7,8]
        ])    
    print(matrix_1)   
    print(f'{(matrix_1==matrix_2)=}')  
    print(f'{(matrix_1==matrix_3)=}')     
    print(f'{(matrix_1>matrix_3)=}')      
    print(f'{(matrix_1<matrix_3)=}')      
    print(f'{(matrix_1<=matrix_3)=}')       
    print(matrix_1+matrix_2) 

    matrix_4 = Matrix([
        [1,2,2],
        [3,1,1]
        ])  
    matrix_5 = Matrix([
        [4,2],
        [3,1],
        [1,5],
        ])     
    print(matrix_4*matrix_5)   
    print(matrix_5*matrix_4)  