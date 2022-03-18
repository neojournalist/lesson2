import datetime
from datetime import date, time, timedelta, timezone, datetime

someText = input('Enter your bio:')
splitted_text = someText.split()
print(splitted_text)
print(splitted_text[0:3])
print(splitted_text[7:])

# Составьте какой-нибудь текст из этого списка объединив при этом
# первые 5 слов с последними 2мя словами

text1 = 'Бишкек@Самый@лучший@город@в@мире'
newText = text1.split('@')
print(newText)

timeNow = datetime.now()
print(timeNow.time())

userDate = input('Enter your date in this format "d-m/yyyy -(H:M:S) " : ')
newDate = datetime.strptime(userDate, '%d-%m/%Y -(%H:%M:%S)')
print(newDate)
print(newDate.strftime('%d-%a-%B-%Y - %H:%M:%S'))

today = datetime.now() - timedelta(60)
print(today)

today1 = datetime.now() - timedelta(730)
print(today1)

today3 = datetime.now() - timedelta(367)
print(today3)

today2 = datetime.now() - timedelta(93)
print(today2)






