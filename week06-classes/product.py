
class Product:
    def __init__(self, id, name, category, stock):
        self.id = id
        self.name = name
        self.category = category
        self.stock = stock

    def received_items(self, n):
        self.stok += n

    def sold_items(self, n):
        if n <= self.stock:
            self.stock -= n
        else:
            print("Not enough stock")

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + self.category + ' ' + str(self.stock)


a = Product('1000', 'PC', 'Electronics', 30)
b = Product('1001', 'Laptop', 'Electronics', 12)
c = Product('2000', 'T-Shirt', 'Clothes', 365)

a.sold_items(60)
print(a)

print(b)
print(c)