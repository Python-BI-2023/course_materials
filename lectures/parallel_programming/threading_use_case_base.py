import time

import keyboard


character = 0
while True:
    print(character)
    time.sleep(1)
    character = keyboard.read_key()