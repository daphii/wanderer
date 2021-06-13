import csv
import sys
import time

with open('../data/dialogue.csv') as dialogue_file:
    dialogue_csv = csv.DictReader(dialogue_file)
    dialogue_data_dict = {}
    for row in dialogue_csv:
        dialogue_data_dict[row['code']] = row
    
#for dialogue in dialogue_data_dict:
    #print(dialogue + " " + str(dialogue_data_dict[dialogue]) + "\n")

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.035)

def speedprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.01)

class Dialogue:

    def __init__(self, code, speaker,msg):
        self.code = code
        self.speaker = speaker
        self.msg = ""
        for x in msg:
            if x == '|':
                self.msg += "\n"
            else:
                self.msg += x

    def __repr__(self):
        return self.msg

    def splashprint(self, breaks=0):
        clean = " " + self.msg
        print(clean)
        if breaks > 0:
            for i in range(breaks):
                print('\n')

    def typeprint(self, breaks=0):
        clean = " " + self.msg
        slowprint(clean)
        if breaks > 0:
            for i in range(breaks):
                print('\n')
            
dialogue_dict = {}
for dialogue in dialogue_data_dict:
    code = dialogue_data_dict[dialogue]['code'] 
    speaker = dialogue_data_dict[dialogue]['speaker']
    msg = dialogue_data_dict[dialogue]['msg']
    dialogue_dict[dialogue] = Dialogue(code, speaker, msg)

#dialogue_dict['07'].typeprint()
#print("\n")
#dialogue_dict['06'].splashprint()

#  Dialogue Sequences

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

dialogue_dict['earthlaunch'] = earthlaunch