import os
from time import sleep
import keyboard

def clear(time=0):
    sleep(time)
    os.system('clear')

def menu():
    opt = 0
    while True:

        menu = f"""
        [{"*" if opt == 0 else ""}] Nouveau
        [{"*" if opt == 1 else ""}] Jouer
        [{"*" if opt == 2 else ""}] Quitter
        """
        print(menu)

        if keyboard.is_pressed('up') and opt != 0: opt -= 1
        if keyboard.is_pressed('down') and opt != 2 : opt += 1

menu()
