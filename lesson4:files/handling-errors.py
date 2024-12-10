from pathlib import Path

def open_file():
    path = Path(__file__).parent
    path = path / 'random' / 'random.txt'

    try:
        file = path.open('r')
        content = file.read()
        print(content)
        file.close()

    except FileNotFoundError as e:
        print(e)
        print(f"{path} doesn't exist")  

    except Exception as ex:
        print(ex)

    return

def main():
    open_file()

if __name__ == "__main__":
    main()