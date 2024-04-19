import threading
import time


def download_data():
    time.sleep(10)
    print("Data downloading")

def process_data():
    print("Data processing")


threads = [threading.Thread(target=download_data) for _ in range(10)]
for thread in threads:
    thread.start()
process_data()
