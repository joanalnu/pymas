# 3. Hot Chocolate Recipe ☕️��

## What You Will Learn
* **Dictionaries**: A way to store paired information (names and values)
* How to look up information in a dictionary
* How to loop through dictionary items

## What You Will NOT Learn

This is not a real recipe—don't try to prepare it!

## Understanding Dictionaries

**Lists** store items in order: `["apple", "banana", "cherry"]`

**Dictionaries** store pairs of information (a key and a value):
- Key: The label or name (like "milk")
- Value: The amount or data (like 200)

## Step 1: Create the File

Call it `hot_chocolate_recipe.py`.

## Step 2: Create the Recipe Information

```python
ingredients = {  # This is a DICTIONARY (curly braces {})
    'chocolate powder': 30,
    'sugar': 5,
    'milk': 200,
}
```

**What's happening here?**

- `{...}` = **Curly braces** mean we're creating a **dictionary**
- `'chocolate powder': 30` = A **key-value pair**. The key is `'chocolate powder'` (a string) and the value is `30` (a number)
- `:` = This separates the key from the value (it means "maps to" or "equals")
- `,` = Commas separate pairs

**A dictionary lets us say:** "The ingredient 'chocolate powder' needs 30 units"

**Keys vs Values:**
- **Keys** are unique labels (like dictionary words)
- **Values** are the data attached to those labels (like word definitions)

## Step 3: Ask for the Number of People

```python
people = int(input("How many people are going to drink? "))
```

This gets a number from the user (converting it from text to an integer, just like in Project 2).

## Step 4: Calculate How Much of Each Ingredient

```python
print('You are going to need...')

for ingredient in ingredients.keys():
    amount = people * ingredients[ingredient]
    print(f'{amount} weight units of {ingredient}')
```

**What's happening here?**

- `for ingredient in ingredients.keys():` = Loop through each **key** in the dictionary. The first time, `ingredient` will be `'chocolate powder'`, then `'sugar'`, etc.
- `ingredients[ingredient]` = This is how we **look up a value** in a dictionary. If `ingredient = 'chocolate powder'`, then `ingredients['chocolate powder']` gives us `30`
- `ingredients[ingredient]` is like saying "what's the value for this key?"
- `people * ingredients[ingredient]` = Multiply the number of people by the amount per person to get the total needed
- `f'{...}'` = This is an **f-string** (formatted string). It lets us put variables inside text using curly braces `{}`

**The trick:** Dictionary keys are like labels that help us find the right value!

## Step 5: Run It!

Try different group sizes!

## Challenges

- How much hot chocolate is each person getting? (Divide total by people)
- Can you add different recipes and a recipe selector with user input?
- What if not everybody wants the same thing?

## Advanced Tip

What if instead of ingredients and quantities, these were names and ages... or products and prices? Get creative and use a dictionary to store any paired data!

## Want more?

### Next project: [4. New Year Countdown 🪩⏳](https://github.com/joanalnu/pymas/blob/main/4_new_year_countdown/GUIDE.md)
