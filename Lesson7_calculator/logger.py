from datetime import datetime

def log(value_1,value_2,operation,result):
    date = datetime.now().strftime('%d/%m/%Y')
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{date};{time};{value_1};{operation};{value_2};{str(result)}\n')