#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def convertIntToBinary(intValue):
    binaryStr = ''
    while intValue > 0:
        binaryStr = str(intValue % 2) + binaryStr
        intValue = intValue // 2
    return binaryStr


print(convertIntToBinary(45)) 
print(convertIntToBinary(3)) 
print(convertIntToBinary(2)) 
 