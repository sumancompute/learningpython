# match case statements -- python version > 3.10

color = input("enter your favourite color : ")

match color:
    case "white":
        print("You are peasceful")

    case "red":
        print("You are dangerous")

    case "blue":
        print("You are intelligent")

    case _:
        print("Unknown personality")