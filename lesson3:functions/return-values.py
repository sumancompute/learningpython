# return values

def square(x):
    return x*x

result = square(5)
print(result)

# returning multiple values

def get_coords():
    x = 25.5
    y = 48.2
    return x,y

result = get_coords()
print(result) # returns the multiple values in the form of tuple
print(*result) # unpacked tuple

a,b = get_coords()
print(a,b)

# Using return to break out of the function
age = 25
def check():
    if age  < 20:
        return
    print(age)

check()