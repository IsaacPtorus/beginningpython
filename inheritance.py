class animal:
    def speak(self):
        print("animal never speaking, ")


# child class
class bee(animal):
    def buzz(self):
        print("the bee busy buzzing,  ")


class duck(bee):
    def quack(self):
        print("ducks always quacking,  ")


a = animal()
a.speak()

b = bee()
b.buzz()
b.speak()

cd = duck()
cd.quack()
cd.buzz()
cd.speak()