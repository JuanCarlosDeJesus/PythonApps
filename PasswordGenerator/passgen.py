import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~` \\"

# Set the options for the password generator. you can exclude any group by setting it to False.
upper, lower, nums, syms = True, True, True, True
# This generator will include uppercase letters, lowercase letters, numbers, and symbols. You cannot reuse any characters.
all = ""

if upper:
    all += uppercase
if lower:
    all += lowercase
if nums:
    all += numbers
if syms:
    all += symbols

# Set the length and amount of passwords to generate. You can change these values as needed.
length = 20
amount = 10

# If you want to generate the same password use seed
# seed = "Fenris"
# random.seed(seed)
# the line above is optional, you can remove it if you want to generate different passwords each time you run the program.

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)



