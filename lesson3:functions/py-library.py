# using random module for example

import random

def main():
    number = random.randint(1, 1000)
    print(f"The random number is : {number}")

    numbers = [1,2,3,4,5,6,7,8]
    random.shuffle(numbers)
    print(f"the shuffled number is : {numbers}")

    return



if __name__ == "__main__":
    main()