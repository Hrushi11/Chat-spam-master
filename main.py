from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()
time.sleep(5)
a = <"Number_of_times_you_want_to_spam"">
while a>0:
    for letter in "<message_you_want_to_spam>":
        Keyboard.press(letter)
        Keyboard.release(letter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    a -= 1

