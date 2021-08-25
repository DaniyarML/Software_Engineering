# generators are automatic version of iterators
# return - terminate the entire function, yield - pauses function & saves the state

def my_gen():
    n = 1
    print('first')
    yield n

    n+=1
    print('second')
    yield n

    n += 1
    print('third')
    yield n

# for i in my_gen():
#     print(i)


def custom_range(start, stop, step=1):
    numbers = []

    while start < stop:
        numbers.append(start)
        start += step

    return numbers

def custom_xrange(start, stop, step=1):

    while start < stop:
        yield start
        start += step

# for i in custom_range(0, 5):
#     print(i)

for i in custom_xrange(0,5):
    print(i)