from datetime import datetime

def get_year_month(line):
    year = line.split()[0].split('.')[0]
    month = line.split()[0].split('.')[1]
    return (int(year),int(month))

def get_meters_text(line):
    period = get_year_month(line)
    meters = line.split()
    result = f"Показания за {period[1]} {period[0]} года.\n\
               Санузел. Горячая вода: {meters[1]}\n\
               Санузел. Холодная вода: {meters[2]}\n\
               Кухня. Горячая вода: {meters[3]}\n\
               Кухня. Холодная вода: {meters[4]}\n"
    return result        

def get_last_data():
    current_year = datetime.now().year
    current_month = datetime.now().month
    with open('meters.txt', 'r') as file:
        lines = file.readlines()
        last_line = lines[-1]
        last_period = get_year_month(last_line)
        if (current_year == last_period[0] and current_month == last_period[1]):                       
            last_line = lines[-2]           
    return get_meters_text(last_line)    

def get_current_data():
    current_year = datetime.now().year
    current_month = datetime.now().month
    with open('meters.txt', 'r') as file:     
        lines = file.readlines()
        last_line = lines[-1]
        last_period = get_year_month(last_line)
        if (current_year == last_period[0] and current_month == last_period[1]):                       
            return get_meters_text(last_line)           
    return False  

def save_to_file(meter_list):    
    current_year = datetime.now().year
    current_month = datetime.now().month
    if get_current_data(): 
        with open('meters.txt', 'r+') as file:  
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            # start writing lines except the last line
            # lines[:-1] from line 0 to the second last line
            file.writelines(lines[:-1])   
    with open('meters.txt', 'a') as file:
        file.write(f'{current_year}.{current_month} {meter_list[0]} {meter_list[1]} {meter_list[2]} {meter_list[3]}\n')              