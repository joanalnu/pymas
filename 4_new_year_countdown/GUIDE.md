# 4. New Year Countdown 🎄⏳

## What You Will Learn

- How to use the `datetime` module
- How to subtract dates
- How to format time differences

## Step 1 — Create the File

Call it `new_year_countdown.py`.

## Step 2 — Get Today’s Date

```python
from datetime import datetime

today = datetime.now()
```

## Step 3 — Create New Year Date

```python
year = today.year
new_year = datetime(year+1, 1, 1)
```

## Step 4 — Show the Difference

```python
time_left = new_year - today

days = time_left.days
seconds = time_left.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60

print(f"🎄 {year+1} is in {days} days, {hours} hours, and {minutes} minutes!")

```

## Challenges

- Count down to New Year’s too
- Print snowflakes while waiting
- Turn into a live countdown that updates every second