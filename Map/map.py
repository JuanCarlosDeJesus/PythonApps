# Map Function - map a function to a list of iterable values

numbers = [14, 23, 8, 12, 2, 5, 90]

# square list without map function
squared_numbers = []

def square(x):
    return x**2

for n in numbers:
    squared_numbers.append(square(n))

print(squared_numbers)

# using list comprehension to square the numbers
squared_numbers_comp = [square(n) for n in numbers] 

print(squared_numbers)

# square list with map function
squared_numbers_map = map(square, numbers)
print(list(squared_numbers_map))

# before list comprehension, map funtion was prefered over the multi-lined way. map function, we can use lambda function to square the numbers
