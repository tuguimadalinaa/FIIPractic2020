import json


def go_keys(data, key):
    if type(data) == dict:
        if len(data) > 1:
            new_string = ""
            for k, v in data.items():
                new_string += str(go_keys(v, str(key) + "." + str(k)))
                new_string += "\n"
            return new_string
        else:
            return [str(key) + "." + str(x[0]) + "." + str(x[1]) for x in data.items()][0]
    return str(key) + "." + str(data)


def print_dict(data):
    for key, value in data.items():
        if type(value) == dict:
            result = go_keys(value, key)
            print(result)
        else:
            print(str(key), end=".")
            print(str(value), end="\n")


if __name__ == "__main__":
    with open('example.json') as f:
        data = json.load(f)
        print_dict(data)
