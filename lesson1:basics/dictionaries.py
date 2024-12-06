#dictionaries

person = {
    "name" : "ram",
    "age" : 30,
    "job" : "chef"
}

print(person)
print(person["age"])

#methods

print(person.get("name"))

print(person.keys()) #dict_keys: returns the list of the keys from dictionary view. it is different from a regular list
print(person.values())

print("age" in person.keys()) #Returns true if age exists as a key in the dictonary else retuns false

#to copy the dictionary to another dictionary

copied_person = person.copy()
print(copied_person)

#to update the dictionary

person.update({"name":"hari", "age":35})
print("Updated person is :",person)
print(copied_person) #the update in person doesn't affect the copied one

#to clear the dictionary

person.clear()
print("Cleared person is", person) #Returns empty data