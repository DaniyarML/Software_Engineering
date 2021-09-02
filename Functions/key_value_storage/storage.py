import argparse
import os
import json
import tempfile

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--value', help='Value')
    return parser.parse_args()

def read_data(storage_path):
    with open(storage_path, 'r') as f:
        file = f.read()
    if file:
        return json.loads(file)
    return {}

def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))

def put_data(storage_path, key, value):
    data = read_data(storage_path)
    if key not in data:
        data[key] = [value]
    else:
        data[key].append(value)
    write_data(storage_path, data)

def get_data(storage_path, key):
    data = read_data(storage_path)
    return data[key]

def main(storage_path):
    args = parse()

    if args.key and args.value:
        put_data(storage_path, args.key, args.value)
    if args.key:
        get_data(storage_path, args.key)
    else:
        raise 'Input at least key...'


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)