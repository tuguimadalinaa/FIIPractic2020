import json

if __name__ == "__main__":
    with open('example.json') as f:
        data = json.load(f)
        print(data)
        print(type(data))
