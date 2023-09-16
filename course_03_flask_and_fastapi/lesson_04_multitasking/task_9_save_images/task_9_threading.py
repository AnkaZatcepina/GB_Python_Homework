from task_9_common import url_to_filename, parse
import requests
import threading
import time
import argparse

def download(url):
    response = requests.get(url)
    filename = 'threading_' + url_to_filename(url)
    with open(filename, "wb") as f:
        f.write(response.content)
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")

if __name__ == '__main__':
    urls = parse()

    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()