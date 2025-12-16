# main.py

# 1. Import the functions you need from the calculator module
from calculator import add, subtract, multiply, divide

# 2. Use the functions and store the results
num1 = 50
num2 = 10

# Addition
sum_result = add(num1, num2)

# Subtraction
difference_result = subtract(num1, num2)

# Multiplication
product_result = multiply(5, 7)

# Division (safe)
try:
    quotient_result = divide(num1, num2)
    zero_division_test = divide(10, 0) # This will cause an error
except ValueError as e:
    # This catches the specific error we built into the divide function
    print(f"Error during division: {e}")
    quotient_result = "N/A"

# 3. Print the results
print("--- Calculator Results ---")
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {difference_result}")
print(f"5 * 7 = {product_result}")
print(f"{num1} / {num2} = {quotient_result}")
print("--------------------------")