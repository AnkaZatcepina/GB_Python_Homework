from task_9_common import url_to_filename, parse
import requests
from multiprocessing import Process, Pool
import time

def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url_to_filename(url)
    with open(filename, "wb") as f:
        f.write(response.content)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

processes = []
start_time = time.time()
if __name__ == '__main__':
    urls = parse()

    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()