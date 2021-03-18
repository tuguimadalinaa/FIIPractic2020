import json


def print_dict(data):
    for key, value in data.items():

        if type(value) == dict:
            if len(value.items()) > 1:
                for k, v in value.items():
                    print(str(key), end=".")
                    print_dict(dict({k: v}))

            else:
                print(str(key), end=".")
                print_dict(value)
        else:
            print(str(key), end=".")
            print(str(value), end="\n")


if __name__ == "__main__":
    with open('example.json') as f:
        data = json.load(f)
        print_dict(data)
