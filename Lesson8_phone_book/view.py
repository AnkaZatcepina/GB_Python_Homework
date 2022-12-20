import phonenumbers

def choose_main_menu():
    print('Это телефонный справочник') 
    print('Выверите номер пункта меню: ')   
    print('1. Вывести весь справочник')  
    print('2. Поиск номеров по фамилии') 
    print('3. Добавление новой записи') 
    print('4. Выход')  
    mode = input('')
    if mode in ('1','2','3','4','5'):
        return int(mode)
    return 'Некорректно введён пункт меню'

def choose_view_menu():
    print('Выберите формат вывода данных')    
    print('1. В командную строку')  
    print('2. Сгенерировать XML')
    mode = input('')
    if mode in ('1','2'):
        return int(mode)
    return 'Некорректно введён пункт меню'


def input_surname_for_search():
    surname = input('Введите фамилию: ')
    return surname        

def input_new_entry():   
    surname     = input('Введите фамилию: ')   
    name        = input('Введите имя: ') 
    phone = ''  
    while phone == '':
        try:
            phone = phonenumbers.format_number(phonenumbers.parse(input('Введите номер телефона: ')), phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        except phonenumbers.NumberParseException:
            print('Некорректно введён телефон')
    description = input('Введите описание: ')
    entry = (surname,name,phone.__str__(),description)
    return entry

def print_phone_book(phone_list):    
    for i in phone_list:
        print(i)

def print_message(message):
    print(message)       