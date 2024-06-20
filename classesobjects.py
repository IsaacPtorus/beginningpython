# A CLASS is a blueprint of an object
# AN OBJECT is an instance of a class

class Person:
    # properties/attributes/variables/characteristics
    name = "Spongebob"
    age = 25
    height = 2.4

    # method/function/behavior
    def walk(self):
        print(Person, " is walking")


accountant = Person()  #creating an object
accountant.walk()

teacher = Person()
teacher.walk()
