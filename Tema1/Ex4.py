import json


def print_dict(data):
    for key, value in data.items():
        print(str(key), end=".")
        if type(value) == dict:
            print_dict(value)
        else:
            print(str(value), end="\n")


if __name__ == "__main__":
    with open('example.json') as f:
        data = json.load(f)
        print_dict(data)
