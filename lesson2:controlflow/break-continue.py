count = 0

# break - break out of the loop

while count < 10:
    if count == 5:
        break
    print(count)
    count += 1

    # prints 0,1,2,3,4

# continue - skip iteration

while count < 10:
    count += 1
    if count % 2 != 0:
        continue
    print(count)

    # prints 2,4,6,8,10