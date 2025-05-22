
class Vehicle:
    def __init__(self, plate, brand):
        self.plate = plate 
        self.brand = brand 
        self.km = 0
        self.rented_to = None 

    def __str__(self):
        return self.brand + " " + self.plate
    

class Car(Vehicle):
    def __init__(self, plate, brand, type):
        super().__init__(plate, brand)
        self.type = type 

    def __str__(self):
        return super().__str__() + " " + self.type

    
class Truck(Vehicle):
    def __init__(self, plate, brand, capacity):
        super().__init__(plate, brand)
        self.capacity = capacity 

    def __str__(self):
        return super().__str__() + " Capacity: " + str(self.capacity)
    

class Motorcycle(Vehicle):
    def __init__(self, plate, brand, usage):
        super().__init__(plate, brand)
        self.usage = usage 

    def __str__(self):
        return super().__str__() + " Usage: " + self.usage
    

v = Car('ZAB6734', 'Yaris', 'Hatchback')
w = Car('YTE9087', 'Tiguan', 'SUV')
z = Truck('AAN9081', 'Volvo', 2.5)
m = Motorcycle('BB768', 'Honda', 'Enduro')

print(v)
print(w)
print(z)
print(m)