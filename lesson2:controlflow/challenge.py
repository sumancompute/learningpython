# make the user input the name and price of the item until they  press 'q' to exit. 
# once the user enters 'q', print the list of the items with the price and also print the total price

shopping_list = []

while True:
    item = input("Enter a item or 'q' to exit : ")

    if item == 'q':
        break

    try:
        price = int(input("Enter the price of the item : "))
    
    except ValueError as e:
        print("Error : ", e)
        continue

    shopping_list.append((item, price))

total = 0
for i,p in shopping_list:
    print(f"{i} -  {p} ")
    total += p
    

print("The total price is : ", total)