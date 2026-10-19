class Bank:
    def __init__(self,n,acc,b,bal):
        self.bank_name = n
        self.account_number = acc
        self.branch = b
        self.balance = bal

obj1 = Bank("SBI", 234345, "pune", 20000 )
obj2 = Bank("HDFC", 1234, "Nagpur", 1500)

print(obj1.bank_name)
print(obj1.account_number)
print(obj1.branch)
print(obj1.balance)

print(obj2.bank_name)
print(obj2.account_number)
print(obj2.branch)
print(obj2.balance)


