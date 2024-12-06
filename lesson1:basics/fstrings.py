# formatted strings (f -s trings)

name = "suman"
score = 50

# newer approach 

print(f"{name} has a score of {score}")

# older approach

print("{} has a score of {}".format(name, score)) # using format method
print("{0} has a score of {1}".format(name, score)) # using index
print("{n} has a score of {s}".format(n=name, s=score)) # assigning value to the variables

# expressions in f-strings

print(f"{name.upper()} has a score of {score*50}")
