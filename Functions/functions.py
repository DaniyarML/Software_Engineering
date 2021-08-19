# simple function
from datetime import datetime

def get_seconds():
    return datetime.now().second

print(get_seconds())

# annotation of the functions
def add(x: int, y: int) -> int:
    return x+y

print(add(10,11))
print(add('still', 'works'))

# function works by key or by value
def extender(source_list, extend_list):
    return source_list.extend(extend_list)

values = [1,2,3,4]
extender(values, [5,6,7])
print(values) # since list is mutable, the object in the memory is changed

def replacer(source_tuple, replace_tuple):
    source_tuple = replace_tuple

user_info = ('Daniyar', 5)
replacer(user_info, ('Dan', 7))
print(user_info)

# it is not recommended to use mutable obj as a default param
def append_one(iterable=[]):
    iterable.append(1)
    return iterable

print(append_one())
print(append_one())
print(append_one.__defaults__)

def append_one(iterable=None):
    iterable = iterable or []

# args
def printer(*args):
    print(type(args))
    for argument in args:
        print(argument)

printer(1,2,3,4,5,6)

name_list = ['John', 'Bill', 'Amy']
printer(*name_list)

# kwargs
def printer(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key, value)

printer(a=10, b=11)
#print(**some_dict)