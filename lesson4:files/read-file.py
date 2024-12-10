# reading file

def read_file():

    # open file
    file = open('characters.txt', 'r') # open characters.txt file in read mode

    # read the file
    content = file.read() # reads the whole file as it is
    print(content)

    lines = file.readlines() # returns each line separately
    for line in lines:
        print(line)

    # close the file
    file.close()

    return


def main():
    read_file()
    return

if __name__ == "__main__":
    main()