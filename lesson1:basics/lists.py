#lists - mutable

names = ["suman", "ganga", "sanam"]
print(names)
print(names[0])
print(names[1])
print("Length of the list is: ", len(names))

#Changing the lists values

names[2] = "sanradhya"
print(names)

#List methods

names.append("ram")
print(names)

names.remove(names[0])
print(names)

names.sort()
print(names)


#joining lists

ages_one = [25, 90, 49, 60, 75]
ages_two = [19, 65, 21, 44, 38]

joined_ages = ages_one + ages_two #we have joined the two lists into a new variable
print("Joined ages is", joined_ages)

ages_one.extend(ages_two) #we have added ages_two in the list of ages_one
print("Extended ages_one is :", ages_one)
print(ages_two) #it doesn't affect ages_two


#slicing list

scores = [100, 99, 25, 44, 85, 77, 64]
print("From start to index 2", scores[:3] )
print("From index 3 to end", scores[3:])
print("From index 1 to 4", scores[1:5])
print("From start to 4 with the step of 2", scores[:5:2])
print("From start to end with the step of 2", scores[::2] )
print("reversing the list", scores[::-1])
