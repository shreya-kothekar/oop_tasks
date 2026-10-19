class Mobile:
    def __init__(self, b, c, p):
        self.brand = b
        self.color = c
        self.price = p

obj1 = Mobile("Oppo", "Blue", 15000)
obj2 = Mobile("Vivo", "Black", 25000)

print(obj1.brand)
print(obj1.color)
print(obj1.price)

print(obj2.brand)
print(obj2.color)
print(obj2.price)