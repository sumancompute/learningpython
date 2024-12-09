score = 7

# if statements

if score>5:
    print('Score is greater than 5')

# if else statements:

if score > 10:
    print('Score is greater than 10')

else:
    print('Score is not greater than 10')

# if/elif/else statements

if score > 10:
    print('Score is greater than 10')

elif score > 5:
    print('Score is greater than 5 but not than 10')

else:
    print('The score is 5 or less')


# and, or, not, is not

age = 18

if age > 12 and age < 20:
    print('You are a teenager')

if age < 13 or age > 19:
    print('You are not a teenager')

authenticated = True

if authenticated:
    print('You are authenticated')

if not authenticated:
    print('You are not authenticated')

if authenticated is not True:
    print('You are not authenticated')