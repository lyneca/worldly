from classes import *
import re

with open("data.wy") as file:
    data = file.read().replace('\n', '').replace(' ', '')

things = Things()
objects = re.findall(r'([\w_]+).([\w_]+)\{([^}]+)?\}', data)
for o in objects:
    things.add(Thing(things, *o))
for thing in things:
    print(thing)
