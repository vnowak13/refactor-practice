
from budget import budgetFunction
from calculator import calculator
from weather import weather
from shopping import shoppingList
from temp import temp_cal
from inventory import store_invent
from password import validate_password
# Create a Function: Turn this logic into a function called suggest_destination(budget) that:

# Accepts budget as an argument.
# Returns the suggestion as a string.
     
budgetFunction(300)

# Instructions for Students:

# Refactor this code by creating a function for each arithmetic operation (e.g., add, subtract, etc.).
# Make a Calculator class that contains these functions as methods.
# Ensure that division checks for zero before attempting the operation.
# Move the arithmetic logic into a file named calculator.py.

calculator(10,5)

####################################################################################################
# Instructions for Students:

# Create a function that takes weather as an argument and returns the appropriate advice.
# Optionally, create a class WeatherAssistant with a method for weather advice.
#Move the weather advice logic into a file named weather_advice.py.

weather("rainy")



# Instructions for Students:

# Refactor this code by creating functions to:
# Add an item to the shopping list.
# Remove an item from the shopping list.
# Print all items in the shopping list.
# Optionally, create a ShoppingList class that manages the list with the above methods.
#Move the shopping list logic into a file named shopping_list.py.

shoppingList([])



# Instructions for Students:

# Refactor this code by creating two functions:
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# Consider creating a TemperatureConverter class with these methods.

temp_cal(22, 88)


# Instructions for Students:

# Create functions for:
# Adding an item to the inventory.
# Removing an item from the inventory.
# Printing the inventory.
# Optionally, organize these into an Inventory class.

store_invent()






# Instructions for Students:

# Refactor this code by creating a validate_password(password) function.
# Extend it to check for additional rules like special characters.

validate_password()