# Try-tries to execute your command ,except-offers an alternative for try and finally-executes regardless of error--
try:
    print(number)


except:
    print("OOH NO!An error occurred")

finally:
    print("Success!We made it through")

x = 67
y = 0
try:
    print(x / y)
except:
    print("Arithmetic error")
finally:
    print("Success??")
