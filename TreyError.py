# not a good practice to use only except
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:  # catches tha error
    print(err)
except ValueError as err:
    print("Invalid input")
