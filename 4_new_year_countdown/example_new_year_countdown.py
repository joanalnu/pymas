# Import the datetime class from the datetime module
# datetime lets us work with dates and times
from datetime import datetime

# Get today's date and time
# datetime.now() is a METHOD (a function attached to datetime)
# It returns the current date and time
today = datetime.now()

# Extract the current year from today's date
# The dot (.) means "get the year attribute from today"
year = today.year

# Create a date object for January 1st of next year
# datetime(year, month, day) creates a date
# year+1 means next year
# 1, 1 means January (month 1), day 1
new_year = datetime(year+1, 1, 1)

# Calculate the time difference between New Year and today
# You can subtract dates to get a timedelta object (time difference)
time_left = new_year - today

# Extract the number of full days remaining
days = time_left.days

# Get the remaining seconds (after counting full days)
# This doesn't include the full days already counted
seconds = time_left.seconds

# Convert seconds to hours
# // is integer division (divides and drops the decimal)
# 3600 seconds = 1 hour
hours = seconds // 3600

# Get the remaining minutes
# % is the modulo operator (gives the remainder)
# (seconds % 3600) gives seconds left after counting full hours
# Then // 60 converts remaining seconds to minutes
minutes = (seconds % 3600) // 60

# Print the countdown message
# f"..." is an f-string (formatted string)
# Curly braces {} insert variables into the message
print(f"🎄 {year+1} is in {days} days, {hours} hours, and {minutes} minutes!")
