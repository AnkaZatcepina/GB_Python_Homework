

def add_new_entry(entry):
    with open('phone_book.csv', 'a') as file:
        file.write(f'{entry[0]};{entry[1]};{entry[2]};{entry[3]}\n')

def get_phone_list():   
    phone_list = []    
    with open('phone_book.csv', 'r') as file:
        for line in file.read().splitlines():
            phone_list.append(line.split(';')) 
    return phone_list    

def filter_by_surname(phone_list, surname):   
    filtered_phone_list = []   
    for entry in phone_list:
        if entry[0] == surname:
            filtered_phone_list.append(entry.copy()) 
    return filtered_phone_list        
