# using w mode to write in the files deletes the previous content.
# so use of append mode to add the content to the previous content

characters = ["suman", "ganga", "sanam", "ram", "hari"]

def write_characters_to_file(filename):
    # open file

    file = open(filename, 'a+') # 'a' mode only writes to file. to read the file, we must use 'a+' mode

    # write to file

    for c in characters:
        file.write(c + "\n") #breaks line after every item

    # close file

    file.close()

    return

def main():
    write_characters_to_file('characters.txt')
    

if __name__ == "__main__":
    main()