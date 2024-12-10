# global and local scope

x = 10

# def print_x():
#     x = 15 # changes the value of x inside the print_x() to 15
#     print(f"Value of x inside the print_x() is : {x}")

def print_x():
    global x # changes the global value of x
    x = 15
    print(f"Value of x inside the print_x() is : {x}")

print_x()

print(f"Global Value of x is : {x}")

def print_y():
    y = 30
    print(f"Value of y inside print_y() is : {y}")

print_y()


# ------------------- 

# scope with nested functions

def outer():
    age = 25;

    def inner():
        nonlocal age #changes the value of age in outer scope as well
        age = 30
        print(f"Age inside inner() is : {age}")
    
    inner()

    print(f"Age inside outer() is : {age}")

outer()