# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

a: int = 10
b: str = 'New string'
c: bool = False

print(type(a))
print(type(b))
print(type(c))

if type(b) == str:
    print('OK')
else:
    print("Not a string")  

if isinstance(c, int):
    print('OK')
else:
    print("Not a string")        