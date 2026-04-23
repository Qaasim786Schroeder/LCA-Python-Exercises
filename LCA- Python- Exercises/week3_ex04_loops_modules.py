# week3_ex04_loops_modules.py

# Question 1: Using a for loop with a list
# TODO: Create a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Mango"]

# TODO: Use a for loop to print each fruit in the list
print("--- Question 1: Fruits ---")
for fruit in fruits:
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown
# TODO: Use a while loop to create a countdown from 5 to 1
print("\n--- Question 2: Countdown ---")
count = 5
while count >= 1:
    print(count)
    count -= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()
# TODO: Use a for loop to print the first 10 square numbers
print("\n--- Question 3: Square Numbers ---")
for i in range(1, 11):
    print(f"{i} squared is {i**2}")

#-------------------------------------------------------------------------
# Question 4: Using the random module
# TODO: Import the random module
import random

# TODO: Create a list of colors
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]

# TODO: Use a for loop to select and print 3 random colors from the list
print("\n--- Question 4: Random Colors ---")
for i in range(3):
    print(random.choice(colors))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module
# TODO: Import the custom module and use its functions
import math_operations

print("\n--- Question 5: Custom Module & Calculator ---")
print(f"Addition test (10 + 5): {math_operations.add(10, 5)}")

# TODO: Use a while loop to create a simple calculator
while True:
    print("\n--- Simple Calculator ---")
    print("Choose operation: +, -, *, / (or type 'exit' to stop)")
    choice = input("Enter choice: ")
    
    if choice.lower() == 'exit':
        print("Exiting calculator...")
        break
        
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print(f"Result: {math_operations.add(num1, num2)}")
    elif choice == '-':
        print(f"Result: {math_operations.subtract(num1, num2)}")
    elif choice == '*':
        print(f"Result: {math_operations.multiply(num1, num2)}")
    elif choice == '/':
        print(f"Result: {math_operations.divide(num1, num2)}")
    else:
        print("Invalid operator.")