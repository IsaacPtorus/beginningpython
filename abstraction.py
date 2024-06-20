from abc import ABC, abstractmethod

# Abstract class (Vehicle)
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def drive(self):
        pass

# Concrete class (Car) inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is being driven.")

# Concrete class (Motorcycle) inheriting from Vehicle
class Motorcycle(Vehicle):
    def drive(self):
        print(f"{self.brand} motorcycle is being driven.")

# Creating objects of concrete classes
my_car = Car("Toyota")
my_motorcycle = Motorcycle("Honda")

# Calling the drive method (abstraction in action)
my_car.drive()  # Output: Toyota car is being driven.
my_motorcycle.drive()  # Output: Honda motorcycle is being driven.





# Abstraction example using abstract base class

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete implementation of Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage of abstraction
# shape = Shape()  # This would raise an error because Shape is an abstract class

circle = Circle(5)
print("Area of circle:", circle.area())
print("Perimeter of circle:", circle.perimeter())
