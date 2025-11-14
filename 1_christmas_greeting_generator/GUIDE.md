# 1. Christmas Greeting Generator 🎅✨

## What You Will Learn
* How to store messages in Python **lists**
* How to pick elements randomly.
* How to print variables.


## Step 1: Create a File

Call it `greeting_generator.py`.

## Step 2: Create a List with Some Holiday Hreetings

```python
greetings = [
    "Merry Christmas!",
    "Happy Holidays!",
    "Warm winter wishes!",
    "Have a magical Christmas season!",
    "May your day be merry and bright!"
]
```

Remember!: Python lists are groups of elements separated by `,` and written between `[]``. They can contain repeated elements and mixed of variable types (integers, strings, ...)

## Step 3: Use `random.choice()` to pick one greeting

```python
import random

message = random.choice(greetings)
print(message)
```

## Step 4: Run it!
Each time you run the program a new greeting appears!

## Challenges
* Add more greetings
* Ask the user for their name and include it in the message

## Advanced Tip
If you are into math and really want to test whether your computer can generate randomness, you can use the random function to pick up numbers. Then you can compare the frequency of your draws with a the fliping of a coin or with a dice.

```python
import random

# for the coin: two possible solutions (0,1)
frequency = 0 # to count how many heads/tails
flips = 10 # the number of flips
for i in range(flips):
    coin = random(0,1)
    frequency + coin

# 1->heads, 0->tails
print(f'The coin flipped {frequency} heads and {flips-frequency} tails.')

# there are 6 numbers in a regular dice
frequency = [0,0,0,0,0,0]
for i in range(flips):
    dice = random(1,2,3,4,5,6)
    frequency[dice]+=1

print(f'The dice flipped:')
print(f'{frequency[1]} times 1')
print(f'{frequency[2]} times 2')
print(f'{frequency[3]} times 3')
print(f'{frequency[4]} times 4')
print(f'{frequency[5]} times 5')
print(f'{frequency[6]} times 6')

```

Pro: can you observe the trick used for keeping up with the frequency in the coin case?

## Want more?

### Next project: [ASCII Christmas Tree 🌲⭐]()