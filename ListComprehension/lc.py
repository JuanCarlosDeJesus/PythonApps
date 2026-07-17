# List Comprehension

numbers = [18,16,22,99,23,11,54]

new_list = []
for n in numbers:
    if n % 2 == 0:
        new_list.append(n)
print(new_list)

# list comprehension
new_list = [n for n in numbers if n % 2 ==0]
print(new_list)

numbers = [1,2,3,4,5,6,7]

power_of_two = [2 ** x for x in numbers]
print(power_of_two)

# you can use range
power_of_two = [2 ** x for x in range(1,8)]
print(power_of_two)

# add if after range
power_of_two = [2 ** x for x in range(1,8) if x % 2 == 0]
print(power_of_two)

# adding else to list comprehension
words = ['automobile', 'car', 'anger', 'fox', 'anchor']

words = [word.upper() if word.startswith('a') else word for word in words]
print(words)