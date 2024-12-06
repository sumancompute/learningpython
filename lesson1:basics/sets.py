# sets - unordered and unique elements

ingredients = {"tofu", "avocado", "cherries", "pasta", "tofu"}
print(ingredients) # Prints tofu only once

# Make a set using the set function around the list

scores = set([100,99,85,100,79])
print(scores) # Prints the 100 only once

# Methods

ingredients.add("tomato")
print(ingredients) # Adds tomato to the set

ingredients.remove("cherries")
print(ingredients) # Remove cherries from the list

# ingredients.remove("apple") # Shows error because apple is not there in the set

ingredients.discard("apple")
print(ingredients) # Doesn't show error even if apple is not there in the set

# Joining sets (Union)

set_one = {1, 2, 3}
set_two = {3, 4, 5}

union_set = set_one.union(set_two)
print(union_set) # Prints {1,2,2,4,5}

# Intersection sets (set of common elements)

int_set = set_one.intersection(set_two)
print(int_set) # Prints {3}

# frozen (immutable) sets - sets are mutable because we can add and remove data from the set, so we use frozen to make it immutable

ages = frozenset([100, 90, 100, 85, 87])
print(ages)
# ages.add(20) # shows error