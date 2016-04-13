import json


def init_file():
    open('data.txt', 'w+').close()


def load_file(file='data.txt'):
    try:
        with open(file, mode='r') as f:
            data = json.loads(f.readline())
            content = f.readlines()
            save_file(content)
        return data
    except json.decoder.JSONDecodeError:
        print("Data is empty")
        return None


def save_file(data):
    with open('data.txt', mode='w') as f:
        f.writelines(data)


def append_file(data):
    with open('data.txt', mode='a') as f:
        f.write(json.dumps(data))
        f.write("\n")
