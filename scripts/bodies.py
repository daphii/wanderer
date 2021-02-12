import csv

with open('../data/bodies.csv') as bodies_file:
    bodies_csv = csv.DictReader(bodies_file)
    bodies_data_dict = {}
    for row in bodies_csv:
        bodies_data_dict[row['name']] = row
    
#for body in bodies_data_dict:
    #print(body + " " + str(bodies_data_dict[body]) + "\n")


class Body:

    def __init__(self, name, state, diameter, parent, distance, orbit, discovered, discoverer, text):
        self.name = name
        self.state = state
        self.diameter = diameter
        self.parent = parent
        self.distance = distance
        self.orbit = orbit
        self.discovered = discovered
        self.discoverer = discoverer
        self.text = text

    def __repr__(self):
        return "{0}: ~{1} km average diameter. Currently orbiting {2} once every {3} Earth days, at a distance of {4} km.".format(self.name, self.diameter, self.parent, self.orbit, self.distance)
            

bodies_dict = {}
for body in bodies_data_dict:
    name = bodies_data_dict[body]['name'] 
    state = bodies_data_dict[body]['state']
    diameter = bodies_data_dict[body]['diameter']
    parent = bodies_data_dict[body]['parent']
    distance = bodies_data_dict[body]['distance']
    orbit = bodies_data_dict[body]['orbit']
    discovered = bodies_data_dict[body]['discovered']
    discoverer = bodies_data_dict[body]['discoverer']
    text = bodies_data_dict[body]['text']
    bodies_dict[body] = Body(name, state, diameter, parent, distance, orbit, discovered, discoverer, text)


#new_var = bodies_dict['Earth']
#print("\n")
#print(new_var.orbit)

