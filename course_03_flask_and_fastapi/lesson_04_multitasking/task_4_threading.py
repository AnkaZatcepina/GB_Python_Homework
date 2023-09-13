"""
    Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
    Используйте потоки.
"""

import os
import threading
import time

PATH = './parser_url/'
count = 0
lock_count = threading.Lock()
        
def count_words(filename: str)->None:
    global count
    with open(filename, "r", encoding='utf-8') as f:
        lock_count.acquire()
        count += len(f.read().split())
        lock_count.release()
    print(f"File {filename} is finished: {count}")  

if __name__ == '__main__':

    threads = []
    start_time = time.time()

    """os.chdir(PATH)
    files = os.scandir()
    for file in files:
        thread = threading.Thread(target=count_words, args=[file.path])
        threads.append(thread)
        thread.start()"""
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            filepath = os.path.join(root, filename)
            thread = threading.Thread(target=count_words, args=(filepath,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
 
    print(f'Result: {count}')    