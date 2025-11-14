ingredients = { # ingredients for a hot chocolate cup
    # again, this are invented values, not a real recipe, so don't try to prepare it!
    'chocolate powder': 30,
    'sugar': 5,
    'milk': 20,
}

people = int(input("How many people are going to drink?"))

print('You are going to need...')

for ingredient in ingredients.keys():
    print(f'{people*ingredients[ingredient]} weight units of {ingredient}')