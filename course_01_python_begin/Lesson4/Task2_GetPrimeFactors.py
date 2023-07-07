#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def getPrimeFactors(n):
    result = []
    while n != 1:
        for i in range(2,n+1):
            if n%i == 0:
                n //= i
                result.append(i)
                break
    return result

print(getPrimeFactors(int(6)))
print(getPrimeFactors(int(5)))