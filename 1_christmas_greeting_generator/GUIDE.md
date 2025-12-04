# 1. Christmas Greeting Generator 🎅✨

## What You Will Learn
* How to store messages in Python **lists**
* How to pick elements randomly
* How to print variables

## Before You Start: A Quick Guide to Data Types

**Variables** are like containers that hold information. In Python, different types of information need different types of containers:

- **Strings**: Text surrounded by quotes (`"like this"` or `'like this'`)
- **Integers**: Whole numbers (5, -3, 100)
- **Lists**: Multiple items grouped together in square brackets `[item1, item2, item3]`

## Step 1: Create a File

Call it `greeting_generator.py`.

## Step 2: Create a List with Some Holiday Greetings

```python
greetings = [
    "Merry Christmas!",
    "Happy Holidays!",
    "Warm winter wishes!",
    "Have a magical Christmas season!",
    "May your day be merry and bright!"
]
```

**What's happening here?**

- `greetings` = This is the **variable name** (the container's label)
- `=` = This means "store the following information in this variable"
- `[...]` = **Square brackets** mean we're creating a **list**
- Each greeting is a **string** (text inside quotes)
- `,` = **Commas** separate items in a list

**Remember!**: Python lists are groups of elements separated by commas and written between `[]`. They can contain repeated elements and can mix different data types (strings, numbers, etc.).

## Step 3: Use `random.choice()` to Pick One Greeting

```python
import random

message = random.choice(greetings)
print(message)
```

**What's happening here?**

- `import random` = We're bringing in Python's random tool. "Import" means "grab this tool and make it available to us"
- `random.choice(greetings)` = Pick one random item from the greetings list
- `message =` = Store that randomly picked greeting in a variable called `message` (now it's a **string**)
- `print(message)` = Show the message on the screen

## Step 4: Run It!

Each time you run the program, a new greeting appears!

## Challenges
* Add more greetings
* Ask the user for their name and include it in the message

## Advanced Tip

If you're interested in math and probability, test whether your computer generates true randomness! You can compare the frequency of random draws with coin flips.

```python
import random

# Flip a coin 100 times and count heads
frequency = 0  # Counter to track heads
flips = 100  # Number of flips

for i in range(flips):
    coin = random.choice([0, 1])  # 0 = tails, 1 = heads
    frequency += coin  # Add 1 to frequency if it's heads

# Print the results
heads = frequency
tails = flips - frequency
print(f'Heads: {heads}, Tails: {tails}')
```

**What's the trick?**
- `frequency += coin` is short for `frequency = frequency + coin`. It adds the result to our counter.
- If you flip 100 times, you should get close to 50 heads and 50 tails (but not exactly!)

## Want more?

### Next project: [ASCII Christmas Tree 🌲⭐](https://github.com/joanalnu/pymas/blob/main/2_ascii_christmas_tree/GUIDE.md)
