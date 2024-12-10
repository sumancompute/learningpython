from pathlib import Path
import json

path = Path(__file__).parent / 'characters.json'

characters = {
    "characters":[
        {"name":"suman", "age":25},
        {"name":"sanma", "age":26},
        {"name":"compute", "age":30}
    ]
}

def read_json():
    with path.open('r') as file:
        data = json.load(file)
    return data

def write_json():
    with path.open('w') as file:
        json.dump(characters, file, indent = 3)
    return

def main():
    write_json()
    data = read_json()
    print(data)

if __name__ == "__main__":
    main()