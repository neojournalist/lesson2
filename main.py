#strings
#word = 'some word'
#word2 = input('Type second word: ')
#print('The lenght of the word:', len(word))

#age = int(input('Enter age: '))
#number1 = 40
#number2 = 65

#totalAge = age + number1
#totalAge2 = totalAge
#print(totalAge)
#print(type(totalAge)) #int
#print('Information from the lesson:\n', word, '\n', age)

poem = """
E lhnth
bfrekg
bjkfekr
"""
print(poem)

if 'bfrekg' in poem:
    print('Yes, it exists')
else:
    print('Not in poem')
#print(word[0])

if 'bfrekg' not in poem:
    print('Does not exist in poem')
else:
    print('Yes, it exists')

#Slicing, метод покускового отображения инфо
#Slicing of strings
#[start:stop:step]
word = 'some word'
word_No_s = word[1:]

print(word[2])
print(word_No_s) #ome word
print(word[2:-2])

#the text in reverse order
print(word[::-1])

#the text full
print(word[:])

word2 = 'Hello There'
print(word2[1:9:2])
print(word2[1:9:3])

#findning index
word3 = 'I live in Bishkek'
print(word3.find('Bishkek'))
print(word3.find('live'))
print(word3.find('love'))

#finding rfind
print(word3.rfind('Bishkek'))

#replacing smt
word3 = word3.replace('Bishkek', 'Kyiv')
print(word3)

word4 = 'I love Bishkek and I study in Bishkek and I live in Bishkek'
print(word4.count('Bishkek'))

#methods
text2 = 'my name is Tina'
print(text2.upper())
upperText = text2.upper()
print(upperText)

lowercaseText = upperText.lower()
print(lowercaseText)

capitalizedText = lowercaseText.capitalize()
print(capitalizedText)

fileName = 'myFile.pdf'
fileName2 = 'myFile.docx'

fileName3 = 'lessonFile.pdf'
fileName4 = 'myLesson.pdf'

if fileName2.endswith('.pdf')
    print('Accepted')
else:
    print('Change your file')

if fileName3.startswith('lessonFile'):
    print('Accepted')
else:
    print('We do not accept this format')

#strip, lstrip, rstrip
longWord = '   Some Text    '
print(longWord)
print(longWord.lstrip())

print(longWord.rstrip())
print(longWord.strip())

someText = '%%%%Do Something%%%%%'
print(someText.lstrip(%))
print(someText.rstrip('%'))
print(someText.strp('%'))

name = input('Your name:')
age = input('Your age:')
gender = input('Your gender:')
job = input('Your company name:')
status = input('Your status:')
address = input('Your address:')

print(len(name))

if 'a' in job:
    print('You have a')
else:
    print('You do not have a')

print(address[2])

print(name[1:])
print(job[::-1])

#formats
name = 'Tina'
age = '28'
info = 'I live and work in Bihskek'

print(name, '\n', age, '\n', info, '\n')
print(name, end=" ")
print(age, end=" ")
print(info, end=" ")

print('Name: {0} Age: {1} Info: {2}'.format(name, age, info))