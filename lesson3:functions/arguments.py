# positional argumenmts

def multiply(a, b):
    return a*b

result = multiply(7, 5)
print(result)

# named arguments

def print_score(name, score):
    print(f"Score of {name} is {score}")

print_score("suman", 50)
print_score(score=75, name="hari") # if given the name to argument, the position or order of arguments doesn't matter

# default argument

def divide(a, b=2):
    return a/b

result = divide(20, 4) # uses the value of b as 4, not as 2
print(result) # 5.0

result = divide(50) # uses the value of b as 2
print(result) #35.0