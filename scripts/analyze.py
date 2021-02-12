import random

from bodies import Body
from bodies import bodies_dict
from forms import Form
from forms import forms_dict

def run(body):

    icy_forms = []
    for form in forms_dict:
        if forms_dict[form].eco == "i":
            icy_forms.append(forms_dict[form])

    rocky_forms = []
    for form in forms_dict:
        if forms_dict[form].eco == "r":
            rocky_forms.append(forms_dict[form])

    for form in forms_dict:
        if forms_dict[form].eco == "b":
            rocky_forms.append(forms_dict[form])
            icy_forms.append(forms_dict[form])
    
    forms_eco_list = [icy_forms, rocky_forms]

    if body.state == "i":
        pick_idx = random.randint(0, len(icy_forms) - 1)
        analysis = icy_forms[pick_idx]

    if body.state == "r":
        pick_idx = random.randint(0, len(rocky_forms) - 1)
        analysis = rocky_forms[pick_idx]

    if body.state == "f" or "u": ### remove the u when this is part of the loop
        eco_type = random.choice(forms_eco_list)
        pick_idx = random.randint(0, len(eco_type) - 1)
        analysis = eco_type[pick_idx]

    if body.state == 's':     ### remove this when it is part of the loop
        analysis = 'special type'


    print(analysis)
    return analysis