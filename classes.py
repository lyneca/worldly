class Things:
    def __init__(self):
        self.objects = []

    def __add__(self, other):
        self.objects.append(other)
        return self

    def __iter__(self):
        return iter(self.objects)

    def add(self, other):
        self.__add__(other)

    def __contains__(self, item):
        if type(item) == Thing:
            if item in self.objects:
                return True
            else:
                return False
        elif type(item) == str:
            if item in [x.name for x in self.objects]:
                return True
            else:
                return False
        else:
            return False

    def __getitem__(self, item):
        if self.__contains__(item):
            for o in self.objects:
                if o.name == item:
                    return o
        else:
            raise IndexError("'" + item + "' not in objects")


def get_type(obj):
    if ',' in obj:
        return [get_type(x) for x in obj.split(',')]
    try:
        int(obj)
    except ValueError:
        return obj
    return int(obj)


class Thing:
    def __init__(self, things, i, n, p):
        self.name = n
        self.inherits = i
        self.properties = {}
        for prop in p.strip(';').split(';'):
            if prop:
                self.properties[prop.split(':')[0]] = get_type(prop.split(':')[1])
        if self.inherits in things:
            self.properties.update(things[self.inherits].properties)

    def __str__(self):
        return self.name + " " + self.inherits + " at " + str(hex(id(self))) + " with properties " + repr(self.properties)


class Usable(Thing):
    def use(self):
        pass
