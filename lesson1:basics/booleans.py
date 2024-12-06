#boolean

is_authenticated = True
print(is_authenticated) #True
print(not is_authenticated) #False

#Comparison operators

x = 5
y = 10

print(x > y) #False
print(x < y) #True
print(x == y) #False
print(x != y) #True
print(x >= y) #False
print(x <= y) #True

#Boolean operators and member checking

x, y = True, False
print(x and y) #False - both needs to be true
print(x or y) #True - at least one needs to be true

#Falsy values -> 0 numbers and empty data structures

print(bool(0)) #False
print(bool("")) #False
print(bool([])) #False

#Truthy values -> everything else

print(bool(1)) #True
print(bool(("Hello", "Suman"))) #True

#Evaluating strings

name = "suman"
print(name.startswith('s')) #True
print(name.startswith('a')) #False
print(name.endswith('n')) #True