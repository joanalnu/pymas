# Import the random module so we can pick things randomly
import random

# Create a LIST of greetings (strings grouped in square brackets)
# Each string is separated by a comma
greetings = [
    "Merry Christmas!",
    "Happy Holidays!",
    "Warm winter wishes!",
    "Have a magical Christmas season!",
    "May your day be merry and bright!"
]

# Use random.choice() to pick ONE random greeting from the list
# random.choice() picks a random item from any list
message = random.choice(greetings)

# Print the randomly selected greeting to the screen
print(message)
