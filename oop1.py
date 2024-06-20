class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def details(self):
        print(self.name, "is studying")

accountant=person("James",43,"male")
print(accountant.name)
print(accountant.age)
print(accountant.gender)

secretary=person("Sarah",32,"female")
print(secretary.name)
print(secretary.age)
print(secretary.gender)

doctor =person("Josef",35,"male")
print(doctor.name)
print(doctor.age)
print(doctor.gender)