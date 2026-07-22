# Lambda functions
mysquare = lambda x: x * x

print(mysquare(5))  # Output: 25

# passing multiple arguments to a lambda function
mysum = lambda a, b: a + b
print(mysum(3, 4))  # Output: 7

# passing a collection to a lambda function
mysum_list = lambda *args: sum(args)
print(mysum_list(1, 2, 3, 4, 5))  # Output: 15

# passing a lambda in a print statement
print((lambda x: x * 2)(10))  # Output: 20

# filtering a list using a lambda function
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# mapping a list using a lambda function
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]

# return a lambda function from another function
def make_incrementor(n):
    return lambda x: x + n

increment_by_5 = make_incrementor(5)
print(increment_by_5(10))  # Output: 15