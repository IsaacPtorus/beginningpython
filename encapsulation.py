class Animal:
    def __init__(self, name, sound, habitat):
        self.name = name
        self.sound = sound
        self.habitat = habitat

    def display_name_and_sound(self):
        return "This animal is a", self.name, "it is" , self.habitat

    def __update_model(self, new_name):
        self.name = new_name

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__update_model(new_name)
        else:
            print("Invalid model name format.")


my_animal = Animal("Donkey", "Brays", "domestic")

print(my_animal.habitat)

print(my_animal.display_name_and_sound())

my_animal.set_name("cat")
print(my_animal.display_name_and_sound())














































#
#
# class Car:
#     def __init__(self, make, model, fuel_type):
#         self.__make = make  # Private attribute
#         self.__model = model  # Private attribute
#         self.fuel_type = fuel_type  # Public attribute
#
#     def display_make_and_model(self):
#         return f"This car is {self.__make} {self.__model}"
#
#     def __update_model(self, new_model):  # Private method
#         self.__model = new_model
#
#     def set_model(self, new_model):
#         if isinstance(new_model, str):
#             self.__update_model(new_model)
#         else:
#             print("Invalid model name format.")
#
#
# # Creating an instance of Car
# my_car = Car("Toyota", "Corolla", "Petrol")
#
# # Accessing public attributes
# print(my_car.fuel_type)  # Output: Petrol
#
# # Accessing private attributes (won't work directly)
# # print(my_car.__make)  # This will raise an AttributeError
#
# # Using public methods to access encapsulated data
# print(my_car.display_make_and_model())  # Output: This car is Toyota Corolla
#
# # Using setter method to update encapsulated data
# my_car.set_model("Camry")
# print(my_car.display_make_and_model())  # Output: This car is Toyota Camry
