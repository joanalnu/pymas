# Import the math module to access mathematical constants and functions
# We'll use math.pi for the sphere volume formula
import math

# Ask the user for the radius of the snowball
# input() gets text from the user
# int() converts it to a number
radius = int(input("How much is the radius of your snowball? "))

# Calculate the volume of the snowball using the sphere formula
# Formula: V = (4/3) * π * r³
# ** is the exponentiation operator (raises to a power)
# radius**3 means r cubed (r × r × r)
# math.pi is the constant π (approximately 3.14159...)
snowball_volume = (4 * math.pi * (radius**3)) / 3

# Print the volume with a message
# f"..." is an f-string that inserts variables with {}
print(f'The volume of the snowball is {snowball_volume} cubic length units.')

# Now calculate how much paper you need to wrap it in a cube box
# The cube must have sides of length 2r to fit the snowball

# Set the side length of the cube (2 times the radius)
a = 2 * radius

# Calculate the area of one side of the cube
# Area of a square = side × side
# We do this twice, not three times, because area is 2D
side_area = a * a

# Calculate the total surface area of the cube
# A cube has 6 faces (sides), so multiply by 6
cube_area = 6 * side_area

# Print how much paper is needed
print(f"You'll need {cube_area} squared length units to wrap up this present!")
