# Question 1: Variable Assignment and String Manipulation
# TODO: Ask the user for their name and age
name = input("Please enter your name: ")
age = input("Please enter your age: ")

# TODO: Print a personalized greeting
print(f"Hello {name}, it is great to meet you! You are {age} years old.")


#-------------------------------------------------------------------------
# Question 2: Integer Operations
# TODO: Ask the user for the length and width of a rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# TODO: Calculate and print the area
area = length * width
print(f"The area of the rectangle is: {area}")


#-------------------------------------------------------------------------
# Question 3: Working with Floats
# TODO: Ask the user for a temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# TODO: Convert to Fahrenheit (Formula: (C * 9/5) + 32)
fahrenheit = (celsius * 9/5) + 32

# TODO: Print the result rounded to 2 decimal places
print(f"The temperature is {round(fahrenheit, 2)} degrees Fahrenheit.")

# Keep window open
input("\nPress Enter to exit...")