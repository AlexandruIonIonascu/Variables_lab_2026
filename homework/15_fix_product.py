# 15 — Fix the product
#
# Read: https://www.w3schools.com/python/python_variables.asp
# Relevant: Creating variables and assigning values.
# Read: https://www.w3schools.com/python/python_casting.asp
# Relevant: int() for whole numbers and float() for decimal numbers.
# Read: https://www.w3schools.com/python/python_operators_arithmetic.asp
# Relevant: Addition, multiplication, and grouping with parentheses.
#
# The starter reads three integers, but it overwrites the same variable.
# Fix it so it stores all three values and calculates their actual product.
# Use distinct, descriptive variable names. Assume valid whole-number inputs.
#
# Inputs 2, 3, 5 must produce: The product is 30
# Inputs 4, 0, 9 must produce: The product is 0

# === YOUR CODE ===
number = int(input("Please type in the first number: "))
number = int(input("Please type in the second number: "))
number = int(input("Please type in the third number: "))
product = number * number * number
print("The product is", product)
