# 2. ASCII Christmas Tree 🌲⭐

## What You Will Learn
* How to use loops
* How to build shapes with text

## Step 1: Create the File

Call it `ascii_tree.py`.

## Step 2: Ask for Tree Height

```python
height = int(input("How tall should your tree be? "))
```

This is taking input from the user and converting the value into an integer. The default variable type delivered by `input()` is a string, not a number!

## Step 3: Build the Tree with a Loop

```python
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

Can you work out home many characters are printed within this loop?

## Step 4: Add a Trunk

```python
print(" " * (height - 1) + "|")
```

## Step 5: Run It!

Try different heights: 3, 5, 10…

## Challenges

- Use `#` instead of `*`
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

## Want more?

### Next project: [3. Hot Chocolate Recipe]()