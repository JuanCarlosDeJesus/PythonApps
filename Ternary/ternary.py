# Ternary operator

age=12  
if age >= 18:
    adult = True
else:
    adult = False

if adult:
    print("You are an adult.")
else:
    print("You are not an adult.")

# ternary operator
adult = True if age >= 18 else False

if adult:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Ternary operator in one line
print("You are an adult.") if adult else print("You are not an adult.")
# or
print("You are an adult." if adult else "You are not an adult.")


number = 9800
# Ternary operator to check if number is even or odd
print("This number is very very large!" if number > 1000 else "This number is quite large!" if number > 100 else "This number is small but still positive!" if number % 2 == 0 else "This number is NOT positive!")