temp = 32
if temp < 25:
    print("Its quite cold")
elif temp > 25:
    print("So hot!")
else:
    print("Huh!Seems temperature is normal")

temp = 25
if temp < 25:
    print("Its quite cold")
elif temp > 25:
    print("So hot!")
else:
    print("Huh!Seems temperature is normal")

    # To return the largest no. among three????
first = 45
second = 75
third = 78
if first > second and first > third:
    print(first, "is the largest")
elif second > first and second > third:
    print(second, "is the largest!")
else:
    print("Hell noo,", third, "is the largest mann!!")

# To determine if a number is even,odd or a zero
firstno = 0
secondno = 75

if firstno == 0:
    print(firstno, "is a zero,which is neither odd nor even")
elif firstno % 2 == 0:
    print("is even")
else:
    print(firstno, "is odd")

if firstno == 0:
    print(secondno, "You entered a zero,which is neither odd nor even")
elif secondno % 2 == 0:
    print("is even")
else:
    print(secondno, "is odd")

# To determine the area of a rectangle
# A=L*W
length = 36
width = 20
area = length * width
print("The Area is", area)

# To determine the area of a trapezium
# area = 0.5 * (base1 + base2) * height
base1 = 5
base2 = 7
height = 4
area = 0.5 * (base1 + base2) * height
print("Area of the trapezium:", area)
