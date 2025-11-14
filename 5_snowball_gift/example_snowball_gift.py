import math

radius = int(input("How much is the radius of your snowball?"))

snowball_volume = (4 * math.pi * (radius**3)) / 3 # formula for the volume of a ball

print(f'The volume of the snowball is {snowball_volume} cubic length units.')

a = 2*radius # length of 1 side of the cube box

side_area = a * a # area of 1 side of the cube

cube_area = 6 * side_area # a cube has 6 sides

print(f"You'll need {cube_area} squared length units to wrap up this present!")