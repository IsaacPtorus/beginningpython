Courses = ["MIT", "Cybersecurity", "Datascience"]  #Same as list
print(Courses)

# Accessing elements in an array
print(Courses[0])
print(Courses[1])
print(Courses[2])

# To add a new element to an array
Courses.append("Android App Dev")  #Also 'pop' adds an element,but in between the others
print(Courses)

# To delete an element from an array
Courses.remove("Cybersecurity")
print(Courses)

# Looping through an array---to display elements as individual items
for course in Courses:
    print(course)
