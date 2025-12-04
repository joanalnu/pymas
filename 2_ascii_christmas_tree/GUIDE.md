# 2. ASCII Christmas Tree 🌲⭐

## What You Will Learn
* How to use **loops** (repeating code)
* How to work with **strings** and text repetition
* How to build shapes with characters

## Understanding Key Concepts

**Loops**: Code that repeats. Instead of writing the same thing many times, loops do it automatically!

**String Multiplication**: In Python, `"*" * 3` creates `"***"` (the string repeats 3 times)

**Integer Division & Modulo**: 
- `//` divides and keeps only the whole number (e.g., `7 // 2 = 3`)
- `%` gives the remainder (e.g., `7 % 2 = 1`)

## Step 1: Create the File

Call it `ascii_tree.py`.

## Step 2: Ask for Tree Height

```python
height = int(input("How tall should your tree be? "))
```

**What's happening here?**

- `input("How tall...")` = Ask the user to type something
- Whatever the user types comes in as a **string** (text). Even if they type "5", it's "5" the text, not 5 the number
- `int(...)` = Convert that text into an **integer** (a number). So "5" becomes 5
- `height =` = Store that number in a variable called `height`

**Why do we need `int()`?** Because we'll use `height` in math calculations, and we need actual numbers, not text!

## Step 3: Build the Tree with a Loop

```python
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

**What's happening here?**

- `for i in range(1, height + 1):` = Start a **loop** that repeats. `i` starts at 1 and goes up to `height` (the colon `:` means "here comes the code that repeats")
- `spaces = " " * (height - i)` = Create a string of spaces. For example, if `height=5` and `i=1`, we get 4 spaces
- `stars = "*" * (2 * i - 1)` = Create stars. For example, if `i=1`, we get 1 star. If `i=2`, we get 3 stars, etc.
- `print(spaces + stars)` = Print the spaces and stars together (the `+` joins them into one line)

**The trick:** Each line has fewer spaces but more stars, creating a triangle shape!

Can you work out how many characters are printed in each line?

## Step 4: Add a Trunk

```python
print(" " * (height - 1) + "|")
```

This adds a simple trunk to the bottom of the tree.

## Step 5: Run It!

Try different heights: 3, 5, 10…

## Challenges

- Use `#` instead of `*`
- Add ornaments as random characters
- Add color using ANSI codes

## Advanced Tip

Can you create other shapes with this technique? Maybe a snowflake...

```python
height = int(input("How big should your snowflake be? "))

for i in range(-height, height + 1):
    line = ""
    for j in range(-height, height + 1):
        if abs(i) == abs(j) or i == 0 or j == 0:
            line += "*"
        else:
            line += " "
    print(line)
```

**What's the trick here?**
- `abs(i)` = Absolute value (the number without the minus sign)
- `or` = Logical operator (it means any of these conditions can be true)
- `+=` = Add to the existing string (short for `line = line + "*"`)

## Want more?

### Next project: [3. Hot Chocolate Recipe ☕️🍫](https://github.com/joanalnu/pymas/blob/main/3_hot_chocolate_recipe/GUIDE.md)
