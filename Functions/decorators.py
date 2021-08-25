
# decorator which logs results
import functools

def logger(func):
    @functools.wraps(func)
    def wrapped(num_list):
        result = func(num_list)

        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)

# print(summator([1,2,3,4,5]))
# print(summator.__name__)
# summator = logger(summator)

def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator


@logger('new_log.txt')
def summator(num_list):
    return sum(num_list)

#print(summator([1,2,3,4,5]))
#summator = logger('new_log.txt')(summator)

# chained decorators

def first_decorator(func):
    def wrapped():
        print('Inside the first decorator')
        return func()
    return wrapped

def second_decorator(func):
    def wrapped():
        print('Inside the second decorator')
        return func()
    return wrapped

@first_decorator
@second_decorator
def printer():
    return 'Hello i am function'

#print(printer())
# printer = first_decorator(second_decorator(printer))

def bold(func):
    def wrapper():
        return '<b>'+func()+'</b>'
    return wrapper

def italic(func):
    def wrapper():
        return '<i>'+func()+'</i>'
    return wrapper

@bold
@italic
def hello():
    return 'hello world'
#hello = bold(italic(hello))
print(hello())