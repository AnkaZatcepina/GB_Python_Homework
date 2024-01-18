def calculate_factorial_imperitive(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial    

def calculate_factorial_declarative(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial_declarative( n - 1)    
