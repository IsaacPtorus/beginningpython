# Datatype
# string-text,float-decimal,boolean-true/false,int-whole

number = 60  #Int
num = 45.65  #Float
greet = "Hello Brother"  #Str
isPythonboring = True  #boolean

Fruits = ["Orange", "Mango", "Pineapple"]  #List----ordered
cars = ("BMX", "Mercedes", "Toyota", "Honda")  #Tuple----unchanged,normal brackets
countries = {"Kenya", "Uganda", "Tanzania"}  #Set
student = {
    "firstname": "Omukhusi",
    "age": "25",
    "course": "MIT",
    "nationality": "Ugandan"
}  #Dictionary

print(num)
print(isPythonboring)
print(Fruits)
print(cars)
print(countries)
print(student["firstname"])
print(student["course"])

'a'  #char single quotes

# To determine datatypes in a variable----
print(type(isPythonboring))
print(type(cars))

#Typecasting????? This is conversion of one datatype to another


print(int(num))
print(float(number))



# for loop  ---counts 1-4
for number in range(1, 4):
    print(number)