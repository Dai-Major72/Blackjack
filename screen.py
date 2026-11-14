import os
from time import sleep
import keyboard

def clear(time=0):
    sleep(time)
    os.system('clear')

def menu():
    opt = 0

    star = lambda _ : "*" if opt == _ else "  "

    while True:
        clear()
        menu = f"""
{star(0)} Player
{star(1)} Select player
{star(2)} Rules
{star(3)} Quit
        """
        print(menu)

        keyboard.read_event()
        if keyboard.is_pressed('up'): opt -= 1
        if opt < 0: opt = 3
        if keyboard.is_pressed('down') : opt += 1
        if opt > 3: opt = 0

        if keyboard.is_pressed('enter') : break

    return opt

def play():
    print("play screen")

def change_player():
    print("player select screen")

def rules():
    print("rule screen")

def quit():
    print("no screen")

menu = menu()

if menu == 0: play()
if menu == 1: change_player()
if menu == 2: rules()
if menu == 3: quit()
