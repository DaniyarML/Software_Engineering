 # inner functions
def get_multiplier() -> object:
    def inner(a,b) -> object:
        return a*b
    return inner

multiplier = get_multiplier()
print(multiplier(10, 11))

#inner
def get_multiplier(number):
    def inner(a):
        return a*number
    return inner

multiplier_by_2 = get_multiplier(2)
print(multiplier_by_2(10))

#map - apply function to ds
def squarify(a):
    return a**2

print(list(map(squarify, range(5))))

#filter - filter by some logic
def is_positive(a):
    return a > 0

print(list(filter(is_positive, range(-2, 5))))

#lambda - short functions (anonymos functions)
print(list(map(lambda x: x ** 2, range(5))))
print(list(filter(lambda x: x > 0, range(-2, 5))))

# list of int to list of string
print(list(map(lambda x: str(x), range(5))))

# list comprehensions
square_list = [i**2 for i in range(5)]
print(square_list)
square_list = [i**2 for i in range(5) if i % 2 == 0]
print(square_list)

# dict comprehension
square_map = {number: number**2 for number in range(5)}
print(square_map)

#zip - join to iterable object
num_list = range(10)
squared_list = [num**2 for num in num_list]
print(list(zip(num_list, squared_list)))