# Ask the user how tall the tree should be
# input() gets text from the user
# int() converts that text into a number (integer)
height = int(input("How tall should your tree be? "))

# Create the tree using a loop
# 'for i in range(1, height + 1):' means repeat this block of code
# i starts at 1 and goes up to height (height is included)
for i in range(1, height + 1):
    # Create spaces for indentation
    # " " * (height - i) means repeat the space character (height - i) times
    # On line 1, we get (height - 1) spaces
    # On line 2, we get (height - 2) spaces, etc.
    spaces = " " * (height - i)
    
    # Create stars for the tree
    # "*" * (2 * i - 1) means repeat the star (2*i - 1) times
    # On line 1: 2*1 - 1 = 1 star
    # On line 2: 2*2 - 1 = 3 stars
    # On line 3: 2*3 - 1 = 5 stars
    # This creates the triangle shape!
    stars = "*" * (2 * i - 1)
    
    # Print the line: spaces first, then stars
    # The + operator joins (concatenates) the two strings together
    print(spaces + stars)

# Add a simple trunk at the bottom
# (height - 1) spaces followed by a vertical bar |
print(" " * (height - 1) + "|")
