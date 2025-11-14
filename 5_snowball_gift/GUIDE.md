# 5. Snowball Gift

## What You Will learn
* Basic geometry
* Formulas with Python

## Step 1: Create the File

Call it `snowball_gift.py`.

## Step 2: Ask for the Snowball Radius

```python
radius = int(input("How much is the radius of your snowball?"))
```

## Step 3: Compute the Volume of the Snowball

```python
import math

snowball_volume = (4*math.pi (r**3))/3 # formula for the volume of a ball

print(f'The volume of the snowball is {snowball_volume} cubic length units.')
```

THe print statement returns the volume in cubic lengths since you can enter the radius of the ball in any length unit (meters, inches, feet, miles, ...).

## Step 4: How much Paper to Wrap it in a Box?

Of course, the box is a cube and has sides length 2r for it to fit the snowball perfectly.

```python
a = 2*radius # length of 1 side of the cube box

side_area = a * a # area of 1 side of the cube

cube_area = 6 * side_area # a cube has 6 sides

print(f"You'll need {cube_area} squared length units to wrap up this present!")
```

Question: Why isn't `cube_area` $a^3$?? What would this expression describe?

## Step 4: Run It!

Try different radiuses!

## Chanllenges

- Let the cube box have a margin?
- How much would the snowball weight (water density is 1)?
- How many snowballs with radius $r/2$ would fit in a box for a snowball of radiius $r$?

## Advanced Tip

How much paper does it take to wrap the snowball itself without putting it into a box? What shape would that be?

What uses more paper sphere or cube box?

How much paper does it take to wrap the snowball into a sphere?

Can you compute the volume to surface area ratio of different shapes (sphere, cube, rectangle, triangle, dodecaedron...)?

## Want more?

### Next project... 

This is the end of the Christmas Python projects series! I hope you enjoyed the holidays and had a good time learning Python coding and maths!

I wish you a prosper New Year and lots of more coding to come! (you can beigin by extending this scripts)