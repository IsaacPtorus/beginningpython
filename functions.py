# Inbuilt functions


y = max(230, 490, 499, 23)
print(y, "is maximum")

x = min(45, 866, 55, 6)
print("The minimum value is", x)

z = pow(23, 6)
print(z)


# range,min,max,


# User-defined functions---
def student():
    print("Glory")


student()  #make sure you call a user defined function


def person():
    print("Persons under cover")


person()


# Parameters and arguments
def add(num1, num2):
    print(num1 + num2)


add(35, 76)
add(48, 49)


def employee(fullname, age, email, maritalstatus, position):
    print(fullname, age, email, maritalstatus, position)


employee("Mark Ojwang", 30, "markojwang@gmail.com", "single", "MD")
employee("Jack Omolo", 56, "jokomolo@gmail.com", "married", "CEO")
employee("Abby Lentii", 34, "ablen@gmail.com", "married", "Secretary")
employee("Osman Masudi", 38, "osmasud@gmail.com", "single", "HR")
employee("Wafula Muraya", 40, "wafmu@gmail.com", "married", "Marketing Man.")
