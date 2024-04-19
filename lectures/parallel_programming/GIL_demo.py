import random
import threading


def do_work():
    for _ in range(100000000):
        random.randint(1, 40) ** random.randint(1, 20)


threads = [threading.Thread(target=do_work) for i in range(2)]
for thread in threads:
    thread.start()

do_work()
