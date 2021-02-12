import random


confirm = "This {0} body is {1} the scope of our current research project."
opt_land = "OPTIMAL LANDING ZONE DETECTED:"
no_record = 'This body has no recorded descriptive characteristics in our database.\nDATABASE UPDATED QUEUED.'
danger = 'DANGER! '
d = "DENIED"
g = "GRANTED"
b = 'beyond'
w = 'within'
c = 'celestial'
r = 'rocky'
f = 'frozen'
i = 'icy'

danger_dict = {
    'r' : ['No safe entry path calculated: Orbital debris exceeding approved threshold.',
           'No safe landing zone: Techtonic activity above approved threshold.',
           'Unsafe surface detected: Slope beyond maximum safe grade.'],
    'i' : ['Unable to find safe landing zone: Possible geyser activity detected.',
           'No safe landing site: Friction levels below calculated minimums.',
           'Unsafe landing site: Rapid melting and refreezing in effect.']
}

safe_dict = {
    'r' : ['Hilltop Overlook',
           'Base of Hill',
           'Rocky Flats',
           'Crater Edge',
           'Crater Basin',
           'Cliff Edge',
           'Base of Cliff',
           'Cave Mouth'],
    'i' : ['Icy Hilltop',
           'Frozen Depression',
           'Dormant Geysers',
           'Icy Cave',
           'Frozen Crater',
           'Hardened Fissures',
           'Glassy Field',
           'Frozen Cliff']
}

def is_safe(body):

    if body.state == 'r':
        check = random.randint(1,10)
        if check > 4:
            return True
        else:
            return False

    if body.state == 'f':
        check = random.randint(1,10)
        if check > 4:
            return True
        else:
            return False

    if body.state == 'i':
        check = random.randint(1,10)
        if check > 4:
            return True
        else:
            return False

def get_safe(body):

    idx = random.randint(0,2)

    if body.state == 'f':
        type_idx = random.randint(0,1)

        if type_idx == 1:
            return safe_dict['r'][idx]
        
        if type_idx == 0:
            return safe_dict['i'][idx]

    if body.state == 'r' or 'i':
        return safe_dict[body.state][idx]    

def get_danger(body):

    idx = random.randint(0,2)

    if body.state == 'f':
        type_idx = random.randint(0,1)

        if type_idx == 1:
            return danger_dict['r'][idx]
        
        if type_idx == 0:
            return danger_dict['i'][idx]

    if body.state == 'r' or 'i':
        return danger_dict[body.state][idx]


def run(body):

    land = 'TOUCHDOWN PERMISSION: '
    can_land = True
    description = ''

    if body.text == '-':
        text = no_record
    else:
        text = body.text

    if body.state == 's':
        land += d + "\n"
        msg = confirm.format(c,b)
        zone = msg

        can_land = False

    if body.state == 'u':
        new_type = random.randint(1,3) - 1
        type_list = ['r', 'f', 'i']
        body.state = type_list[new_type]

    if body.state == 'r':
        
        if is_safe(body):
            land += g + "\n"
            msg = confirm.format(r,w)
            zone = get_safe(body)
            description = opt_land + "\n" + zone
        
        else:
            land += d
            msg = ''
            zone = get_danger(body)
            description = danger + "\n" + zone
            can_land = False

    if body.state == 'f':
        if is_safe(body):
            land += g + "\n"
            msg = confirm.format(f,w)
            zone = get_safe(body)
            description = opt_land + "\n" + zone
        else:
            land += d
            msg = ''
            zone = get_danger(body)
            description = danger + "\n" + zone
            can_land = False

    if body.state == 'i':
        if is_safe(body):
            land += g + "\n"
            msg = confirm.format(f,w)
            zone = get_safe(body)
            description = opt_land + "\n" + zone
        else:
            land += d
            msg = ''
            zone = get_danger(body)
            description = danger + "\n" + zone
            can_land = False               

    print("INFO:" + "\n" + text + "\n")
    if description != '':
        print(description + "\n")
    print(land + msg)

    # True if safe, False if danger/special
    if can_land == False:
        return [can_land, body.name, zone]

    if can_land == True:
        return [can_land, body.name, zone]


