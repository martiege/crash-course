


try:
    number = int(input("Write a number: "))
except ValueError as error: 
    print(error)
    print("Not a number")
except: 
    print("Some other mistake")
else:
    print("The number is:", number)
finally:
    print("Done")


