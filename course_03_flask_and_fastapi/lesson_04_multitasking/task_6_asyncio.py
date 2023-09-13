"""
    Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
    Используйте асинхронный подход.
"""
import os
import asyncio
import time

PATH = './parser_url/'
count = 0

async def count_words(filename: str)->None:
    global count
    with open(filename, "r", encoding='utf-8') as f:
        #lock_count.acquire()
        count += len(f.read().split())
        #lock_count.release()
    print(f"File {filename} is finished: {count}") 

async def main():
    tasks = [] 

    for root, dirs, files in os.walk(PATH):
        for filename in files:
            filepath = os.path.join(root, filename)
            task = asyncio.create_task(count_words(filepath))
            tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())

    print(f'Result: {count}')  