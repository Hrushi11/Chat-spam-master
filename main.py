from pynput.keyboard import Key, Controller
import time1

Keyboard = Controller()
time.sleep(5)
while True:
    for letter in "<message_you_want_to_spam>":
        Keyboard.press(letter)
        Keyboard.release(letter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

