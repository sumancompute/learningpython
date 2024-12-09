# example without error handling

# number = int(input("enter a number")) --- if any letter or word is entred instead of number, then it shows ValueError. So:

# use of try except.
# try is a block of code with potential error. except handles the error. finally is the block of code that executes anyhow
try:
    number = int(input("enter a number"))
    print("You entered : ", number)

except ValueError as e:
    print("That is not a number")
    print("Error : ", e)

finally:
    print("Completed")

# Example 2

a = 10
b = 0

try:
    print(a/b)

except ZeroDivisionError as e:
    print('Cannot divide a number with 0')
    print("Error : ", e)
