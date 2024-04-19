import threading
import time

import keyboard


class KeyboardListener(threading.Thread):
    def __init__(self, active_character):
        super().__init__()
        self.active_character = active_character

    def run(self):
        while True:
            self.active_character = keyboard.read_key()
            if self.active_character == "esc":
                return


character = "0"
listener = KeyboardListener(character)
listener.start()
while True:
    print(character)
    time.sleep(1)
    character = listener.active_character
