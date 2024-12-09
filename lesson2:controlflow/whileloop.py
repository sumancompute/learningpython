# while loop

score = 0

while score < 10:
    print('The score is : ', score)
    score += 1

user_input = ""

while user_input != "q":
    user_input = input("Enter a letter or 'q' to exit")
    print("The letter you entered is : ", user_input)