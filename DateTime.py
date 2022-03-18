import datetime
from datetime import date, time, timedelta, datetime
import locale
#locale.setlocale(locale.LC_ALL, "ru")

someday = date(2010,12,10)
print(someday)
print(f'Month: {someday.month}')
print(f'Day: {someday.day}')
print(f'Year: {someday.year}')

#today = datetime.date.today()
today = date.today()
print(today)

#print(f'Today: Day is {today.day} and month is {today.month} and current year is {today.year}'
 #     f'and hour is {today.hour} and {today.minute} min')

#now = datetime.now()
#print(now)
#print(now.date())
#print(now.time())
#print(now.day())

somedate2 = datetime.strptime('04-12-2018', '%d-%m-%Y')
print(somedate2)

#dateuser = input('Input some date in this format (d:m:yyyy): ')
#somedate3 = datetime.strptime(dateuser, '%d:%m:%Y')
#print(somedate3)

# strftime()
now = datetime.now()

print(now.strftime('%d-%a-%B-%Y %H:%M:%S'))
# strp(извлекаем из текстового формата, но не сможем извлекать. Отвечает только за отображение готовой даты) VERSUS strf()
dateText = '5/5/2022*14$14:14'
dateParsing = datetime.strptime(dateText, '%d/%m/%Y*%H$%M:%S')
print(dateParsing)

#Timedelta
deadline = datetime(2022,5,6)
print(deadline - datetime.now())

day_after_10days = datetime.now() + timedelta(10)
day_after_10daysTime = datetime.now() + timedelta(10) + timedelta(hours=5) + timedelta(minutes=40)
print(day_after_10daysTime)

day_before_yesterday = datetime.now() - timedelta(2)

if now > deadline:
    print('Deadline has passed')
else:
    print(f'It is not over yet')

summer = datetime.strptime('1/6/2022', '%d/%m/%Y')
untilSummer = summer - now
print(f'Until summer: {untilSummer}')

#месяц после 20 мая 2011 года

date1 = date(2011,5,20)
monthLater = date1 + timedelta(30)
print(monthLater)


