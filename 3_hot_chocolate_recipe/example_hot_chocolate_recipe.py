# Create a DICTIONARY to store the recipe information
# Dictionaries use curly braces {} and store key-value pairs
# The key is the ingredient name, the value is the amount needed (per serving)
ingredients = {
    'chocolate powder': 30,
    'sugar': 5,
    'milk': 200,
}

# Ask the user how many people will drink the hot chocolate
# int() converts the text input to a number
people = int(input("How many people are going to drink? "))

# Print a header message
print('You are going to need...')

# Loop through each ingredient in the dictionary
# ingredients.keys() gets all the ingredient names (the keys)
# Each time through the loop, 'ingredient' becomes the next key
for ingredient in ingredients.keys():
    # Look up the amount for this ingredient using square brackets []
    # ingredients[ingredient] gets the value (amount) for this key
    # Then multiply by the number of people
    amount = people * ingredients[ingredient]
    
    # Print how much of each ingredient is needed
    # The f before the quotes makes it an f-string (formatted string)
    # The curly braces {} put variables into the message
    print(f'{amount} weight units of {ingredient}')
