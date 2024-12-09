# for loop with lists - iterate a collection or range

names = ["suman", "ram", "hari", "shiva"]

for name in names:
    print(name)

print("....")

for name in names:
    if name == "hari":
        break
    print(name)
    
print("....")

for name in names:
    if name == "suman":
        continue
    print(name)

print("....")

# for loop with strings

for letter in "suman":
    print(letter.upper())