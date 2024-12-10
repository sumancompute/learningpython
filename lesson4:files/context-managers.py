# context managers -- auto closes the file

from pathlib import Path

def open_file():
    path = Path(__file__).parent / 'characters.txt'
    data = ["apple", "bananan", "peach"]
    # context managers

    with path.open('w+') as file:
        for character in data:
            file.write(character + "\n")
        file.seek(0,0)
        content = file.read()
        print(content)

    return

def main():
    open_file()

if __name__ == "__main__":
    main()