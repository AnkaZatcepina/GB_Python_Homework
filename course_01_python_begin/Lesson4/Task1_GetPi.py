#Вычислить число Пи c заданной точностью d
import math

def getPi(accuracy):
    s = str(accuracy)
    signs = abs(s.find('.') - len(s)) - 1
    return math.floor(math.pi * 10 ** signs) / 10 ** signs

print(getPi(0.0001))    