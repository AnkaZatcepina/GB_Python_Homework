# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
isEqual = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
            check = (not(x or y or z) == (not(x) and not(y) and not(z)))
            if check:
               print('Верно') 
            else:
               print('Ложно')
               isEqual = False
if isEqual:
   print('Утверждение истинно')  
else:
    print('Утверждение ложно')               
