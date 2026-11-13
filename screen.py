import os
from time import sleep
import keyboard

def clear(time=0):
    sleep(time)
    os.system('clear')

def menu():
    opt = 0
    while True:
        clear()
        menu = f"""
        [{"*" if opt == 0 else ""}] Nouveau
        [{"*" if opt == 1 else ""}] Jouer
        [{"*" if opt == 2 else ""}] Quitter
        """
        print(menu, opt)

        sleep(0.08)
        if keyboard.is_pressed('up'): opt -= 1
        if opt < 0: opt = 2
        if keyboard.is_pressed('down') : opt += 1
        if opt > 2: opt = 0
menu()
