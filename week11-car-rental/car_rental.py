
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
    

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name 

    def __str__(self):
        return str(self.id) + " " + self.name
    

class CarRental:
    def __init__(self):
        self.fleet = []
        self.customers = []

    def add_vehicle(self, v):
        self.fleet.append(v)

    def add_customer(self, c):
        self.customers.append(c)

    def display_all(self):
        for v in self.fleet:
            print(v)

    def display_avaliable(self):
        for v in self.fleet:
            if v.rented_to is None:
                print(v)

    def rent_car(self, cid, plate):
        for v in self.fleet:
            if v.plate == plate:
                v.rented_to = cid 

    def get_back(self, plate, km):
        for v in self.fleet:
            if v.plate == plate:
                v.rented_to = None
                v.km = km
    


cr = CarRental()

cr.add_vehicle(Car('ZAB6734', 'Yaris', 'Hatchback'))
cr.add_vehicle(Car('YTE9087', 'Tiguan', 'SUV'))
cr.add_vehicle(Truck('AAN9081', 'Volvo', 2.5))
cr.add_vehicle(Motorcycle('BB768', 'Honda', 'Enduro'))

cr.add_customer(Customer(1, 'james'))
cr.add_customer(Customer(2, 'peter'))
cr.add_customer(Customer(3, 'ann'))
cr.add_customer(Customer(4, 'tom'))
cr.add_customer(Customer(5, 'nancy'))
cr.add_customer(Customer(6, 'oliver'))

while True:
    print("========================")
    print("1. Rent")
    print("2. Return")
    print("3. Display")
    print("0. Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        id = int(input("User ID: "))
        cr.display_avaliable()
        plate = input('Plate: ')
        cr.rent_car(id, plate)
    elif choice == 2:
        plate = input('Plate: ')
        km = int(input("km: "))
        cr.get_back(plate, km)
    elif choice == 3:
        cr.display_all()
    elif choice == 0:
        break;
