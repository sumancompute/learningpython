#declaring variables

name = "suman"
age = 24
height = 5.4

#printing variables

print(name, age, height)

#type errors

# print (name +  " is " + age) cannot conatenate string with integer

print(name + " is " + str(age))


#string methods

greeting = "  Hello, World!  "
print(greeting)
print(len(greeting)) #prints the length of string
print(greeting.strip()) #strips the extra spaces at edges
print(greeting.strip().lower()) #prints string to lowercase
print(greeting.upper().strip()) #prints string to uppercase
print(greeting.replace("World", "Suman").strip()) #replaces the word world by suman
print(greeting) # prints the same result without altering the value because above methods are called as non-destructive methods 