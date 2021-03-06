import json

def to_json(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapped

@to_json
def get_data():
    return {
        'data': 42
    }

if __name__ == '__main__':
    print(get_data())