#tuples

scores = (100, 95, 92, 92, 88, 85)
print(scores)
print(scores[0])
print("Length of the tuple is :", len(scores))

#immutable tuples

# scores[0] = 100 - shows error becaue tuples cannot be changed

#tuples methods

print(scores.count(92)) #prints the number of times 92 is repeated in the tuple
print(scores.index(92)) #prints the first index of 92 in the tuple