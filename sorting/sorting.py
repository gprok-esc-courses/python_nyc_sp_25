data = [3, 56, 1, 23, 12, 67, 4, 10, 100, 6, 71, 8, 19]

sdata = sorted(data)

print(data)
print(sdata)

students = [
    ['Peter', 76], ['Ann', 87], ['Jim', 90], ['Tom', 64], ['Mary', 100]
]

students.sort(key=lambda x: x[1], reverse=True)

print(students)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 

    def __str__(self):
        return self.name + " " + str(self.price)


products = [
    Product('Milk', 45), Product('Cheese', 14), Product('Juice', 60), Product('Bread', 11)
]

products.sort(key=lambda x: x.price, reverse=True)
for product in products:
    print(product)