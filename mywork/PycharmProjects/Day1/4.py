import datetime
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
date2_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date2_entry.split('-'))
date2 = datetime.date(year, month, day)
diff=date2-date1
print (diff.days)