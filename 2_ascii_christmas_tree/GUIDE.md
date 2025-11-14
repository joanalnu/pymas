# 2. ASCII Christmas Tree 🌲⭐

## What will you learn?
* How to use loops
* How to build shapes with text

## Step 1 — Create the File

Call it `ascii_tree.py`.

## Step 2 — Ask for Tree Height

```python
height = int(input("How tall should your tree be? "))
```

## Step 3 — Build the Tree with a Loop

```python
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

## Step 4 — Add a Trunk

```python
print(" " * (height - 1) + "|")
```

## Step 5 — Run It!

Try different heights: 3, 5, 10…

## Challenges

- Use `#` instead of `*`
- Add ornaments as random characters
- Add color using ANSI codes