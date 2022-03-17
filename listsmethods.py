text = 'I love programming and its cool'
splitted_text = text.split()
print(splitted_text)
print(splitted_text[4])

text2 = 'I live in Bishkek. I am 28 years old. My profession is programming.'
listText = text2.split('.')
print(listText)

text3 = 'I live in Bishkek, I am 28 years old, My profession is programming.'
listText3 = text3.split(',')
print(listText3)

text4List = text3.split(' ',2)
print(text4List)

text5List = 'I, live, in, Bishkek, I, am 28 years old. My profession is programming.'
text6List = text5List.split(',',3)
print(text6List)

text7List = text5List.split(',')
print(text6List)
# join Method

mytext = '-'.join(text7List)
print(mytext)
print(type(mytext))

text2 = 'I live in Bishkek. I am 28 years old. My profession is programming.'
newText = '#'.join(text2)
print(newText)
