class student:
    def __init__(self, firstname, course, language):
        self.firstname = firstname
        self.course = course
        self.language = language

    def sleep(self):
        print(self.firstname, "is always late")


cf = student("Caleb", "web dev", "Python")
print(cf.firstname)
print(cf.course)
print(cf.language)
cf.sleep()

masud = student("Masud", "MIT", "Java")
print(cf.firstname)
print(cf.course)
print(cf.language)
masud.sleep()
