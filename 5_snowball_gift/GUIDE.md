# 5. Snowball Gift ❄️🎁

## What You Will Learn
* How to use **modules** (the `math` module with constants and functions)
* How to use mathematical formulas in Python
* Understanding exponents (`**`)

## Understanding Exponents and Operators

- `**` = Exponentiation (raising to a power). `2**3` means 2³ = 8
- `*` = Multiplication
- `/` = Division (always gives a decimal result)
- `//` = Integer division (gives only the whole number)
- `(` `)` = Parentheses force Python to calculate what's inside first

## Step 1: Create the File

Call it `snowball_gift.py`.

## Step 2: Ask for the Snowball Radius

```python
radius = int(input("How much is the radius of your snowball? "))
```

Get a number from the user for the radius (just like in previous projects).

## Step 3: Compute the Volume of the Snowball

```python
import math

snowball_volume = (4 * math.pi * (radius**3)) / 3

print(f'The volume of the snowball is {snowball_volume} cubic length units.')
```

**What's happening here?**

- `import math` = Import Python's math toolbox (it has special constants like π)
- `math.pi` = The constant π (approximately 3.14159...). The `.` means "get pi from the math toolbox"
- `radius**3` = Raise the radius to the power of 3 (cube it)
- The whole formula is: (4 × π × r³) / 3 = Volume of a sphere
- The result is in **cubic units** (because we cubed the radius). So if radius is in meters, volume is in cubic meters!

## Step 4: How Much Paper to Wrap It in a Box?

The box is a cube with sides of length 2r (twice the radius) so the snowball fits perfectly.

```python
a = 2 * radius  # One side of the cube box

side_area = a * a  # Area of one square side (a 2D measurement)

cube_area = 6 * side_area  # A cube has 6 sides

print(f"You'll need {cube_area} squared length units to wrap up this present!")
```

**What's happening here?**

- `a = 2 * radius` = Each side of the cube is twice the radius
- `side_area = a * a` = Area of one square face (length × width). We multiply it twice, not three times!
- `cube_area = 6 * side_area` = A cube has 6 faces, so multiply by 6
- The result is in **squared units** (because area is 2D). If radius is in meters, the area is in square meters!

**Question:** Why isn't `cube_area` equal to a³? What would a³ describe instead? (Hint: that's the volume of the cube!)

## Step 5: Run It!

Try different radii and see how the volume and surface area change!

## Challenges

- What if the cube box needs extra space (a margin) to close it? How much bigger should it be?
- How much would the snowball weigh? (Hint: water density is 1 unit per cubic unit, so volume = weight)
- How many snowballs with radius r/2 would fit inside a box for a snowball of radius r?

## Advanced Tip

How much paper does it take to wrap the snowball itself without putting it into a box? What shape would that be? (Surface area of a sphere!)

What uses more paper: a sphere or a cube box?

Can you compute the volume to surface area ratio of different shapes (sphere, cube, rectangle, triangle, dodecahedron...)?

## Want more?

### Next project...

This is the end of the Christmas Python projects series! I hope you enjoyed the holidays and had a great time learning Python coding and math!

I wish you a prosperous New Year and lots more coding to come! (You can begin by extending these scripts!)
