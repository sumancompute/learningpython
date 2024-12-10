# use of pathlib module

from pathlib import Path

def create_path():
    # script_dir = Path(__file__)
    # print(script_dir) # prints the current file location
    # print(script_dir.parent) # prints the parent directory of the current file

    script_dir = Path(__file__).parent

    path = script_dir / 'characters' # adding characters directory to the above directory

    path.mkdir(parents=True, exist_ok=True) # creating directory characters

    # creating the file inside the directoty

    path1 = path / 'name.txt'
    path2 = path / 'details.txt'

    # open the file in write mode

    file1 = path1.open('w+')

    # write to the file

    file1.write("Shiva")

    # read from the file

    file1.seek(0,0)
    content = file1.read()
    print(content)

    # using different methods

    path2 = path / 'details.txt'

    path2.write_text("student")
    content = path2.read_text()
    print(content)

    # close the file

    file1.close()

def main():
    create_path()

if __name__ == "__main__":
    main()