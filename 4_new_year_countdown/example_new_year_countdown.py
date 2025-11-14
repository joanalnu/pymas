from datetime import datetime

today = datetime.now()

year = today.year
new_year = datetime(year+1, 1, 1)

time_left = new_year - today

days = time_left.days
seconds = time_left.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60

print(f"🎄 {year+1} is in {days} days, {hours} hours, and {minutes} minutes!")
