dte = raw_input("Enter the date in dd-mm-yy format : ")

dte = dte.split("-")

day = dte[0]
year = dte[2]

month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}

month = month_dict[int(dte[1])]
print day, month, "20"+year
