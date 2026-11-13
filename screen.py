import os
from time import sleep
import keyboard

def clear(time=0):
    sleep(time)
    os.system('clear')

def menu():

    def star(p):
        return "*" if opt == p else ""

    opt = 0
    while True:
        clear()
        menu = f"""
[{star(0)}] Play
[{star(1)}] Change player
[{star(2)}] Rules
[{star(3)}] Quit
        """
        print(menu)

        press = keyboard.read_event()
        if press.event_type == keyboard.KEY_UP : opt -= 1
        if opt < 0: opt = 3
        if press.event_type == keyboard.KEY_DOWN : opt += 1
        if opt > 3: opt = 0
        opt = round(opt)
menu()
