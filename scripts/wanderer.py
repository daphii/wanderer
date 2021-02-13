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

print("\n")

#now = datetime.now()
#now_sec = now.strftime("%S")


bodies_key_list = list(bodies_dict.keys())
random_test_name = bodies_key_list[random.randint(0, len(bodies_key_list) - 1)]

random_test_body = bodies_dict[random_test_name]
test_body = bodies_dict['Sol']

#print("\n")
#print(random_test_name)
#sample = scan(random_test_body)
#print("\n")
#print(sample)

forms_key_list = list(forms_dict.keys())
random_test_name = forms_key_list[random.randint(0, len(forms_key_list) - 1)]

random_test_form = forms_dict[random_test_name]
test_form = forms_dict['form zero']

#print("\n")
#print(random_test_form)
#sample = scan(random_test_form)
#print("\n")
#print(sample)
    

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

def earthlaunch():
    for i in range(30,-1,-1):
        output = str(i)
        
        if output == '30':
            dialogue_dict['8'].typeprint()
        
        elif output == '16':
            dialogue_dict['9'].typeprint()
        
        elif output == '10':
            dialogue_dict['10'].typeprint()
        
        elif output == '6':
            dialogue_dict['11'].typeprint()
        
        elif output == '0':
            dialogue_dict['12'].typeprint()
            dialogue_dict['13'].typeprint(2)
            time.sleep(2)
            dialogue_dict['14'].splashprint()
            time.sleep(4)
            dialogue_dict['15'].splashprint()
            time.sleep(4)
            dialogue_dict['16'].splashprint()
            time.sleep(4)
            dialogue_dict['17'].splashprint()

        else:
            clean = " " + output
            slowprint(clean)
            time.sleep(.9)

play = 1
brakes = 0
menu_code = 1
first_load = 1
while play == 1:
    
    # main menu first load
    while menu_code == 1 and first_load == 0:
        clear()
        time.sleep(.5)
        dialogue_dict['1'].typeprint()
        speedprint(art_dict['aurora'])
        dialogue_dict['2'].typeprint()
        choice_list('play', 'credits', 'exit')
        first_load = 1
        user = input('---{ ')

        if user == '1':
            menu_code = 6
            play = 2

        if user == '2':
            menu_code = 2

        if user == '3':
            menu_code = 5

    # main menu consecutive load
    while menu_code == 1 and first_load == 1:
        clear()
        dialogue_dict['1'].splashprint()
        print(art_dict['aurora'])
        dialogue_dict['2'].splashprint()
        choice_list('play', 'credits', 'exit')
        user = input('---{ ')

        if user == '1':
            menu_code = 6
            play = 2

        if user == '2':
            menu_code = 2

        if user == '3':
            menu_code = 5    
    
    # credits menu
    while menu_code == 2:
        clear()
        dialogue_dict['1'].splashprint()
        print(art_dict['aurora'])
        dialogue_dict['2'].splashprint()
        choice_list('art & game credits', 'bibliography', 'back')
        user = input('---{ ') 

        if user == '1':
            menu_code = 3

        if user == '2':
            menu_code = 4

        if user == '3':
            menu_code = 1

    # art & game credits
    while menu_code == 3:
        clear()
        dialogue_dict['3'].splashprint(1)
        dialogue_dict['4'].splashprint(1)
        choice_list('back')
        user = input('---{ ')

        if user == '1':
            menu_code = 2

    # bibliography     
    while menu_code == 4:
        clear()
        dialogue_dict['5'].splashprint(1)
        choice_list('back')
        user = input('---{ ')

        if user == '1':
            menu_code = 2

    # exit screen
    while menu_code == 5:
        clear()
        dialogue_dict['6'].splashprint(1)
        choice_list('exit', 'back')
        user = input('---{ ')

        if user == '1':
            menu_code = 0
            play = 0

        if user == '2':
            menu_code = 1
        
while play == 2:

    while menu_code == 6:
        clear()
        time.sleep(2)
        dialogue_dict['7'].typeprint(2)
        time.sleep(2)
        earthlaunch()
        time.sleep(6)
        clear()


        