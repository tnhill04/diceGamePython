import datetime



today = datetime.date.today()
future = datetime.date(2021, 4, 4)
diff = future - today
print(diff.days)