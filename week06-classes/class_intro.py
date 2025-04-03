
class Car:
    def __init__(self, plate, brand, km):
        self.plate = plate
        self.brand = brand
        self.km = km
        self.rented = False

    def __str__(self):
        return self.plate + ' - ' + self.brand


a = Car('AAZ6786', 'Toyota', 5671)
b = Car('BAB9071', 'Peugot', 9870)

print(a)
print(b)
