import calendar
from calendar import TextCalendar, HTMLCalendar
import pytz
from datetime import datetime

myCalendar = TextCalendar(calendar.MONDAY)
myYearCal = myCalendar.formatmonth(2022,4)
print(myYearCal)

htmlCal = HTMLCalendar(calendar.MONDAY)
myYearCal2 = htmlCal.formatmonth(2022,3)
print(myYearCal2)

for day in myCalendar.itermonthdays(2022,4):
    print(day)

for day in myCalendar.itermonthdates(2022,4):
    print(day)

for days in myCalendar.itermonthdays(2021,2):
    print(days)

for days in calendar.day_name:
    print(days)

for month in calendar.month_name:
    print(month)

myListsW = [day for day in calendar.month_name]
print(myListsW)

now = datetime.now()
print(now)

nowUTCTime = datetime.now(pytz.UTC)
print(nowUTCTime)

nowUSTime = datetime.now(pytz.timezone('US/Central'))
print(nowUSTime)

#for i in pytz.all_timezones:
#    print(i)

nowUSTime = datetime.now(pytz.timezone('Asia/Bishkek'))
print(nowUSTime)
