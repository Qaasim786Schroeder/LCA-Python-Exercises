# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["Apple", "Banana", "Mango"]

# TODO: Add a fruit to the end of the list
fruits.append("Orange")

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "Strawberry")

# TODO: Remove a fruit from the list
fruits.remove("Banana")

# TODO: Print the modified list
print("Modified Fruit List:", fruits)


#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# TODO: Create a new list with each number squared
# Using a list comprehension for efficiency
squared_numbers = [num**2 for num in numbers]

# TODO: Find the sum and average of the original numbers
total_sum = sum(numbers)
average = total_sum / len(numbers)

# TODO: Print the results
print(f"Original Numbers: {numbers}")
print(f"Squared Numbers: {squared_numbers}")
print(f"Sum: {total_sum}, Average: {average}")


#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
capitals = {
    "South Africa": "Pretoria",
    "France": "Paris",
    "Japan": "Tokyo"
}

# TODO: Add a new country-capital pair
capitals["Brazil"] = "Brasilia"

# TODO: Update the capital of an existing country
capitals["South Africa"] = "Cape Town"  # Updating to one of the capitals

# TODO: Remove a country-capital pair
del capitals["France"]

# TODO: Print the modified dictionary
print("Modified Capitals Dictionary:", capitals)


#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Grape": "Purple"
}

# TODO: Print all the fruits (keys)
print("Fruits (Keys):", list(fruit_colors.keys()))

# TODO: Print all the colors (values)
print("Colors (Values):", list(fruit_colors.values()))

# TODO: Print each fruit and its color
print("Fruit and Color pairings:")
for fruit, color in fruit_colors.items():
    print(f"- The {fruit} is {color}")

# TODO: Check if a fruit is in the dictionary and print its color
search_fruit = "Apple"
if search_fruit in fruit_colors:
    print(f"Check: The color of {search_fruit} is {fruit_colors[search_fruit]}.")
else:
    print(f"Check: {search_fruit} was not found.")