# 3. Hot Chocolate Recipe

## What You Will Learn
* Dictionaries in Python
* Fractions in Python

## What You Will NOT Learn
This is not a real recipe, don't try to prepare it!!

## Step 1: Create the File

Call it `hot_chocolate_recipe.py`.

## Step 2: Create the Recipe Information

```python
ingredients = { # ingredients for a hot chocolate cup
    # again, this are invented values, not a real recipe, so don't try to prepare it!
    'chocolate powder': 30,
    'sugar': 5,
    'milk': 20,
}
```

A dictionionary is a variable that enables you to create a list of paired values: keys and values.

## Step 3: Ask for the People

```python
people = int(input("How many people are going to drink?"))
```

## Step 4: How much of each?

```python
print('You are going to need...')

for ingredient in ingredients.keys():
    print(f'{people*ingredients[ingredient]} weight units of {ingredient}')
```

You use dictionaries like `value = dict_name[key]` to call the value assigned to a key.

## Step 5: Run It!

Try different group sizes!

## Challenges

- How much hot chocolate are each of the poeple getting?
- Can you add different recipes and a recipe selector with user input?
- What if not everybody wants the same thing?

## Advanced Tip

What if instead ingredients and quantities these were present and names... Get creative!

## Want more?

### Next project: [4. New Year Countdown]()