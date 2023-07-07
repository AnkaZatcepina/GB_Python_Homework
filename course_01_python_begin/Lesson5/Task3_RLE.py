#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def pack(string):
    packed_string = ""
    old_letter = ""
    count = 0
    for i, letter in enumerate(string):
        if letter != old_letter and i != 0:
            packed_string += str(count) + old_letter
            count = 1
        else:
            count += 1   
        old_letter = letter
    packed_string += str(count) + old_letter    
    return packed_string

def unpack(string):
    unpacked_string = ""
    count = 0
    for letter in string:
        if letter.isnumeric():
            count = count * 10 + int(letter)
        else:
            unpacked_string += letter * count
            count = 0          
    return unpacked_string    

packed_str = pack("AAABCCDDDDDDDDDDDDDEEEEE")
print(packed_str) 
print(unpack(packed_str))  