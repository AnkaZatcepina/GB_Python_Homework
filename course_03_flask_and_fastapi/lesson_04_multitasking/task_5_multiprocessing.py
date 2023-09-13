"""
    Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
    Используйте процессы.
"""

import os
import multiprocessing 
import time

PATH = './parser_url/'
count = multiprocessing.Value('i', 0)
lock_count = multiprocessing.Lock()


def count_words(filename: str, count: multiprocessing.Value)->None:
    with open(filename, "r", encoding='utf-8') as f:
        #lock_count.acquire()
        with count.get_lock():
            count.value += len(f.read().split())
        #lock_count.release()
    print(f"File {filename} is finished: {count}")  

if __name__ == '__main__':

    processes = []
    start_time = time.time()

    for root, dirs, files in os.walk(PATH):
        for filename in files:
            filepath = os.path.join(root, filename)
            process = multiprocessing.Process(target=count_words, args=(filepath, count))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()
 
    print(f'Result: {count.value}')    