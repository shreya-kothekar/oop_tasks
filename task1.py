class MobileShop:
    def __init__(self,n,l,e):
        self.shop_name = n
        self.location = l
        self.employees = e

obj1 = MobileShop("Shree Mobile", "Pune", 4)
obj2 = MobileShop("Raj Mobile", "Mumbai", 8)

print(obj1.shop_name)
print(obj1.location)
print(obj1.employees)

print(obj2.shop_name)
print(obj2.location)
print(obj2.employees)
