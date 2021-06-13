import os
import sys
import time
import random
from datetime import datetime

from bodies import Body
from bodies import bodies_dict
from forms import Form
from forms import forms_dict
from dialogue import Dialogue
from dialogue import dialogue_dict
from dialogue import slowprint
from dialogue import speedprint
from art import art_dict

from scan import run as scan
from analyze import run as analyze

# window sizing (working, keep off for testing in hyper)
os.system("mode con lines=35 cols=80")
# screen clearing
clear = lambda: os.system('cls')

def choice_list(opt1, opt2=None, opt3=None, opt4=None, opt5=None, opt6=None, opt7=None, opt8=None, opt9=None, opt0=None):
    print("[1] - " + str(opt1))
    count = 1
    if opt2 != None:
        print("[2] - " + str(opt2))
        count += 1
    if opt3 != None:
        print("[3] - " + str(opt3))
        count += 1
    if opt4 != None:
        print("[4] - " + str(opt4))
        count += 1
    if opt5 != None:
        print("[5] - " + str(opt5))
        count += 1
    if opt6 != None:
        print("[6] - " + str(opt6))
        count += 1
    if opt7 != None:
        print("[7] - " + str(opt7))
        count += 1
    if opt8 != None:
        print("[8] - " + str(opt8))
        count += 1
    if opt9 != None:
        print("[9] - " + str(opt9))
        count += 1
    if opt0 != None:
        print("[0] - " + str(opt0))
        count += 1
    return count

def display(menu):
    for item in menu:
        print(item)

def slowdisplay(menu):
    for item in menu:
        item.typeprint

menu = True
intro = False

brakes = 0
menu_code = 1.1
first_load = False  # Leave as False for testing

# Main Menu
while menu == True:
    
    # main menu first load
    while menu_code == 1.1 and first_load == True:
        clear()
        time.sleep(.5)
        dialogue_dict['1'].typeprint()
        speedprint(art_dict['aurora'])
        dialogue_dict['2'].typeprint()
        choice_list('play', 'credits', 'exit')
        first_load = False
        user = input('---{ ')

        if user == '1':
            menu_code = 2.0
            intro = True
            menu = False

        if user == '2':
            menu_code = 1.2

        if user == '3':
            menu_code = 1.5

    # main menu consecutive load
    while menu_code == 1.1 and first_load == False:
        clear()
        dialogue_dict['1'].splashprint()
        print(art_dict['aurora'])
        dialogue_dict['2'].splashprint()
        choice_list('play', 'credits', 'exit')
        user = input('---{ ')

        if user == '1':
            menu_code = 2.0
            intro = True
            menu = False

        if user == '2':
            menu_code = 1.2

        if user == '3':
            menu_code = 1.5    
    
    # credits menu
    while menu_code == 1.2:
        clear()
        dialogue_dict['1'].splashprint()
        print(art_dict['aurora'])
        dialogue_dict['2'].splashprint()
        choice_list('art & game credits', 'bibliography', 'back')
        user = input('---{ ') 

        if user == '1':
            menu_code = 1.3

        if user == '2':
            menu_code = 1.4

        if user == '3':
            menu_code = 1.1

    # art & game credits
    while menu_code == 1.3:
        clear()
        dialogue_dict['3'].splashprint(1)
        dialogue_dict['4'].splashprint(1)
        choice_list('back')
        user = input('---{ ')

        if user == '1':
            menu_code = 1.2

    # bibliography     
    while menu_code == 1.4:
        clear()
        dialogue_dict['5'].splashprint(1)
        choice_list('back')
        user = input('---{ ')

        if user == '1':
            menu_code = 1.2

    # exit screen
    while menu_code == 1.5:
        clear()
        dialogue_dict['6'].splashprint(1)
        choice_list('exit', 'back')
        user = input('---{ ')

        if user == '1':
            menu = False
            menu_code = 0

        if user == '2':
            menu_code = 1.1
        
while intro == True:

    # Intro Launch Sequence
    while menu_code == 2.0:
        clear()
        time.sleep(2)
        dialogue_dict['7'].typeprint(2)
        time.sleep(2)
        dialogue_dict['earthlaunch']()
        time.sleep(1)
        clear()
        menu_code = 2.1

    # Good Morning Wanderer
    while menu_code == 2.1:
        pass
        


        