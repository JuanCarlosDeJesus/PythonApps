# F-String
name="Mike"
age=25

# Using old string formatting  %s for string and %d for integer
print("My name is %s and I am %d years old." % (name, age))

# Using str.format() method
print("My name is {} and I am {} years old.".format(name, age))

# Using + method
print("My name is " + name + " and I am " + str(age) + " years old.")

# Print the formatted f-string
print(f"My name is {name} and I am {age} years old.")
# you can also use expressions inside f-strings
print(f"My name is {name.upper()} and I will be {age + 1} years old next year.")
# you can add if statements inside f-strings
print(f"My name is {name} and I am {'old' if age >= 18 else 'not old'}.")

# you can format numbers inside f-strings
pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}.")  # :.2f formats the number to 2 decimal places