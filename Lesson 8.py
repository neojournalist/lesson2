#Lesson 1
#age = int(input(("Your age: ")))
#address = input('Your address: ')
#name = input('Your name: ')

#print(f'Your age is {age}')
#print('Your age is {0} and your address is {1}'.format(age,address))
#print('Attention the person with name  {0} we are departing right now to {1}. We are departing {1} '.format(name, address))

#print('Attention the person with name  {a} we are departing right now to {b}. We are departing {b} '.format(a=name, b=address))

#Lesson 2
#text = 'becoming'
#text1 = text.upper()
#print(text1)

#print(text.capitalize())
#print(text.lower())

#text3 = 'My name is Ascar'

#if 'Ainura' not in text3:
#    print('No')
#else:
#    print('Yes')

#cityName = input('Enter your city: ')

#print(cityName.startswith('B'))
#if cityName.startswith('B'):
#    print('Your city starts with B')
#else:
#    print('Your city does not start with B')

#if cityName.endswith('kek'):
#    print('Your city is Bishkek')
#else:
#    print('your city is false')

progLang = 'Python Django Course'
print(progLang[0:6])
print(progLang[7:])
print(progLang[0:13:2])
print(progLang[::-1])

text5 = '      something'
print(text5.lstrip())
print(text5.strip())

text6 = '&&&text%%%'
print(text6.lstrip('&').rstrip('%'))

userText = input('Enter a word: ')
userText2 = userText.lower()
if userText2 == userText2[::-1]:
    print(True)
else:
    print(False)

word = 'Lesson Python'

for i in range(5):
    print(word)

count = 1
while count <= 5:
    print(word)
    count += 1

