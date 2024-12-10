# writing data to files

characters = ["suman", "ganga", "sanam", "ram", "hari"]

def write_characters_to_file(filename):
    # open file

    file = open(filename, 'w+') # 'w' mode only writes to file. to read the file, we must use 'w+' mode

    # write to file

    for c in characters:
        file.write(c + "\n") #breaks line after every item
    
    # read the file using 'w+' mode
    # however, it doesn't show any content, because after writing to the file, the cursor is placed at the end
    # so use of seek() method to place cursor at the beginning position

    file.seek(0,0)

    content = file.read()
    print(content)

    # close file

    file.close()

    return

def main():
    write_characters_to_file('characters.txt')
    

if __name__ == "__main__":
    main()