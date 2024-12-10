# use *args to accept any number of positional arguments

def print_total(*args):
    print(args) # packed tuple
    print(*args) # unpacked tuple

    total = 0
    for n in args:
        total += n
    print(f"The total is : {total}")

print_total(1,2,3)
print_total(1,2,3,4,5)

# use *kwargs to accept any number of keyword arguments

def print_name(**kwargs):
    print(kwargs) # dictionary

    for key, value in kwargs.items():
        print(f"{key} -- {value}")

    return

print_name(fname="suman", age=25, height=5.4)
print_name(lname="compute")