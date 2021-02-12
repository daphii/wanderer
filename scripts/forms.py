import csv

with open('../data/forms.csv') as forms_file:
    forms_csv = csv.DictReader(forms_file)
    forms_data_dict = {}
    for row in forms_csv:
        forms_data_dict[row['name']] = row
    
#for form in forms_data_dict:
    #print(form + " " + str(forms_data_dict[form]) + "\n")

class Form:

    def __init__(self, name, eco, core, scan, meta, comp, repro, deve, auto, weight):
        self.name = name
        self.eco = eco
        self.core = core
        self.scan = scan
        self.meta = meta
        self.comp = comp
        self.repro = repro
        self.deve = deve
        self.auto = auto
        self.weight = weight

    def __repr__(self):
        return self.core
            

forms_dict = {}

for form in forms_data_dict:

    name = forms_data_dict[form]['name'] 
    eco = forms_data_dict[form]['eco']
    core = forms_data_dict[form]['core']
    scan = forms_data_dict[form]['scan']
    meta = forms_data_dict[form]['meta']
    comp = forms_data_dict[form]['comp']
    repro = forms_data_dict[form]['repro']
    deve = forms_data_dict[form]['deve']
    auto = forms_data_dict[form]['auto']
    weight = forms_data_dict[form]['weight']

    forms_dict[form] = Form(name, eco, core, scan, meta, comp, repro, deve, auto, weight)


#new_var = forms_dict['form three']
#print("\n")
#print(new_var)