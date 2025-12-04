# 4. New Year Countdown 🪩⏳

## What You Will Learn

- How to use the `datetime` **module** (a built-in Python tool for working with dates and times)
- How to subtract dates to find the difference
- How to work with the time difference

## Understanding Modules

A **module** is like a toolbox that Python provides. We use `import` to grab the tools we need.

`from datetime import datetime` means: "Get the `datetime` tool from the datetime toolbox"

## Step 1: Create the File

Call it `new_year_countdown.py`.

## Step 2: Get Today's Date

```python
from datetime import datetime

today = datetime.now()
```

**What's happening here?**

- `from datetime import datetime` = Import the `datetime` class from the `datetime` module
- `datetime.now()` = Get the current date and time right now
- `today =` = Store it in a variable called `today`

**The `.now()` part:** This is a **method** (a function attached to `datetime`). Think of it as an action: "give me the current date and time now"

## Step 3: Create a Date for New Year

```python
year = today.year  # Extract just the year number from today's date
new_year = datetime(year+1, 1, 1)  # Create a date: January 1st of next year
```

**What's happening here?**

- `today.year` = Extract just the **year** from the date. The `.` means "get me the year from today's date"
- `year+1` = Add 1 to the year (so if it's 2024, we get 2025)
- `datetime(year+1, 1, 1)` = Create a new date object. The numbers are (year, month, day)

## Step 4: Show the Time Difference

```python
time_left = new_year - today  # Subtract one date from another!

days = time_left.days  # How many full days are left?
seconds = time_left.seconds  # How many seconds are left (after counting full days)?
hours = seconds // 3600  # Convert seconds to hours
minutes = (seconds % 3600) // 60  # Get remaining minutes

print(f"🎄 {year+1} is in {days} days, {hours} hours, and {minutes} minutes!")
```

**What's happening here?**

- `new_year - today` = Subtract dates! This tells us the difference between them
- `time_left.days` = Get the number of days from this time difference
- `//` = This is **integer division** (divide and throw away the decimal). So `3661 // 3600` gives `1` (1 hour)
- `%` = This is the **modulo operator** (the remainder). So `3661 % 3600` gives `61` (61 seconds left over)
- `f"...{variable}..."` = An **f-string** that puts variables into your message

## Challenges

- Count down to Christmas too
- Write the remaining time in ASCII
- Turn into a live countdown that updates every second

## Advanced Tip

Can you create a code to input a date and output the remaining time in years, months, days, seconds?

## Want more?

### Next project: [5. Snowball Gift ❄️🎁](https://github.com/joanalnu/pymas/blob/main/5_snowball_gift/GUIDE.md)
