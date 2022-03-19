import calendar
from calendar import TextCalendar, HTMLCalendar
import pytz
from datetime import datetime

userYear = int(input('Enter your year: '))
userMonth = int(input('Enter your month: '))
userDay = int(input('Enter your day: '))
myCal = TextCalendar(calendar.TUESDAY)
userCal = calendar.month(userYear, userMonth, userDay)
print(userCal)

for days in myCal.itermonthdays(userYear, userMonth):
    print(days)

htmlCal = HTMLCalendar(calendar.TUESDAY)
myYearCal = htmlCal.formatmonth(userYear, userMonth)
print(myYearCal)

userDateTime = input('Enter date and time: ')
somedate1 = datetime.strptime(userDateTime, '%d/%m/%Y %H:%M:%S')
#somedate1 = datetime.now(pytz.timezone('Europe/Paris')) #тут не получается
print(somedate1)

print("""Выберите страну для отображения его времени:
1. Франция
2. Япония
3. Австралия
4. Южная Африка
5. Индия """)

country = int(input('Выбор: '))

if country in range(0,6):
    if country == 1:
        print(datetime.now(pytz.timezone('Europe/Paris')))
    elif country == 2:
        print(datetime.now(pytz.timezone('Japan')))
    elif country == 3:
        print(datetime.now(pytz.timezone('Australia/Canberra')))
    elif country == 4:
        print(datetime.now(pytz.timezone('Africa/Johannesburg')))
    elif country == 5:
        print(datetime.now(pytz.timezone('Indian/Reunion')))
else:
    print('N/A')
