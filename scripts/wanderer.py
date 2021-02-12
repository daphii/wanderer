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

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./40)

def slowdisplay(menu):
    for item in menu:
        item.typeprint

def earthlaunch():
    for i in range(30,-1,-1):
        output = str(i)
        
        if output == '30':
            dialogue_dict['08'].typeprint()
        
        elif output == '16':
            dialogue_dict['09'].typeprint()
        
        elif output == '10':
            dialogue_dict['10'].typeprint()
        
        elif output == '6':
            dialogue_dict['11'].typeprint()
        
        elif output == '0':
            dialogue_dict['12'].typeprint()
            dialogue_dict['13'].typeprint()
            time.sleep(1)
            dialogue_dict['14'].splashprint()
            time.sleep(4)
            dialogue_dict['15'].splashprint()
            time.sleep(4)
            dialogue_dict['16'].splashprint()
            time.sleep(6)
            dialogue_dict['17'].splashprint()

        else:
            slowprint(output)
            time.sleep(.9)

menu1 = [dialogue_dict['01'], art_dict['aurora'], dialogue_dict['02']]
menu2 = [dialogue_dict['06']]
menu3 = [dialogue_dict['03'], '\n', dialogue_dict['04'], '\n']
menu4 = [dialogue_dict['05'], '\n']


play = 1
brakes = 0
menu_code = 1
while play == 1:
    
    while menu_code == 1:
        clear()
        display(menu1)
        choice_list('play', 'credits', 'exit')
        user = input('---{ ')

        if user == '1':
            menu_code = 5
            play = 2

        if user == '2':
            clear()
            display(menu1)
            choice_list('art & game credits', 'bibliography', 'back')
            user = input('---{ ')

            if user == '1':
                menu_code = 3

            if user == '2':
                menu_code = 4

            if user == '3':
                menu_code = 1

        if user == '3':
            menu_code = 2
    
    while menu_code == 2:
        clear()
        display(menu2)
        print("\nenter 'exit' to terminate program or 'menu' to return to tha main menu")
        user = input('---{ ')

        if user == 'exit':
            menu_code = 0
            play = 0

        if user == 'menu':
            menu_code = 1

    while menu_code == 3:
        clear()
        display(menu3)
        choice_list('main menu')
        user = input('---{ ')

        if user == '1':
            menu_code = 1

    while menu_code == 4:
        clear()
        display(menu4)
        choice_list('main menu')
        user = input('---{ ')

        if user == '1':
            menu_code = 1
        
while play == 2:

    while menu_code == 5:
        clear()
        time.sleep(2)
        dialogue_dict['07'].typeprint()
        time.sleep(2)
        earthlaunch()
        time.sleep(6)
        clear()


        