class Book:
    def __init__(self, tit, aut, pg):
        self.title = tit
        self.author = aut
        self.pages = pg

obj1 = Book("Python", "Guido van Rossum", 200)
obj2 = Book("Java", "James Gosling", 500)

print(obj1.title)
print(obj1.author)
print(obj1.pages)

print(obj2.title)
print(obj2.author)
print(obj2.pages)