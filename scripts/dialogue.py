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
    time.sleep(1./40)

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

    def splashprint(self):
        print(self.msg)
        print('\n')

    def typeprint(self):
        slowprint(self.msg)
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

