class Laptop:
    def __init__(self, b, r, p):
        self.brand = b
        self.ram = r
        self.price = p

obj1 = Laptop("HP", "8GB", 45000)
obj2 = Laptop("ASUS", "10GB", 55000)

print(obj1.brand)
print(obj1.ram)
print(obj1.price)

print(obj2.brand)
print(obj2.ram)
print(obj2.price)
