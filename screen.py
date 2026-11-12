import os
from time import sleep
import keyboard

def clear(time=0):
    sleep(time)
    os.system('clear')

def menu():

    def up():
        return keyboard.is_pressed('up')

    def change_sel(menu_list, dir):
        for o in menu_list:
            if dir : menu_list["*"]

    while True:
        opt = {
            "1":"*",
            "2":...,
            "3":...
        }
        menu = f"""
        [{opt["1"]}] Nouveau
        [{opt["2"]}] Jouer
        [{opt["3"]}] Quitter
        """
        select_opt = str(1)

        print(menu)
        up = keyboard.is_pressed('up')
        down = keyboard.is_pressed('down')

        if up :
            opt.update([])

menu()

#blblb
