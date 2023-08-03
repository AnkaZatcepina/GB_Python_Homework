"""
    📌 Прочитайте созданный в прошлом задании csv файл без
    использования csv.DictReader.
    📌 Распечатайте его как pickle строку.
"""
import csv
import pickle

def csv_to_pickle(path_csv: str)->None:
    with open(path_csv,'r',encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, dialect='excel')
        data_list = []
        headers = []
        for i, row in enumerate(csv_reader):
            if not i:
                headers = row
            else:
                row_data = {key: value for key, value in zip(headers,row)}  
                data_list.append(row_data)
    print(pickle.dumps(data_list))
    print(data_list)

if __name__ == '__main__':
    csv_to_pickle('task_6_file.csv')         