print("list of months : january, february, march, april, may, june, july, august, september, october, november, december")
month_name = input("input the name of month")
if month_name == "february":
    print("no. of days: 28/29 days")
elif month_name in ("april", "june", "september", "november"):
    print("no. of days: 30 days")
elif month_name in ("january", "march", "may", "july", "august", "october", "december"):
    print("no. of days: 31 days")
else: 
    print("wrong month name")
