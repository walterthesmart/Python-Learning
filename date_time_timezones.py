import datetime
today = datetime.date.today()
print(today)

print(today.weekday())
print(today.isoweekday())

time_delta = datetime.timedelta(days=7)

print(today + time_delta )

bday = datetime.date(2024, 3,15)

till_bday = bday - today
print(till_bday.total_seconds())

t = datetime.time