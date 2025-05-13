class Animal:
    def __init__(self, name):
        self.name = name
        self.diseases = []
        self.valid_food = []
        self.feeding_time = None 

    def __str__(self):
        d = ', '.join(disease for disease in self.diseases)
        f = ', '.join(food for food in self.valid_food)
        return self.name + ", Specie: " + type(self).__name__ + "\nDiseases: " + d + "\nFood: " + f + "\nFeed Time: " + str(self.feeding_time)


class Carnivore(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.valid_food = ['Meat']


class Lion(Carnivore):
    def __init__(self, name):
        super().__init__(name)
        self.valid_food = ['Beef', 'Deer', 'Rabbit']
        self.feeding_time = '10:30'

class Tiger(Carnivore):
    def __init__(self, name):
        super().__init__(name)
        self.valid_food = ['Buffalo', 'Beef', 'Lamp']
        self.feeding_time = '12:00'

class Dolhin(Carnivore):
    def __init__(self, name):
        super().__init__(name)
        self.valid_food = ['Fish', 'Shrimps']
        self.feeding_time = '14:30'



class Area:
    def __init__(self, name):
        self.name = name
        self.animals = [] 
        self.environment = None

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        a = ', '.join(x.name + ' ' + type(x).__name__ for x in self.animals)
        return "AREA " + self.name + " - Animals: " + a


class OpenSpace(Area):
    def __init__(self, name):
        super().__init__(name)
        self.environment = 'Savana'

class Pool(Area):
    def __init__(self, name):
        super().__init__(name)
        self.environment = 'Salty water'


class Zoo:
    def __init__(self):
        self.areas = []

    def add_area(self, area):
        self.areas.append(area)

a = Lion("Simba") 
a.diseases.append('kidney failure')
print(a)

b = Tiger("Katy") 
b.diseases.append('teeth decay')
print(b)

c = Dolhin("Willy")
print(c)

ar = OpenSpace('34')
ar.add_animal(a)
ar.add_animal(b)

print(ar)

ar2 = Pool('P2')
ar2.add_animal(c)

print(ar2)

z = Zoo()
z.add_area(ar)
z.add_area(ar2)