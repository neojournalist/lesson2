myTuple = ()
myTuple2 = tuple()
print(type(myTuple))
print(type(myTuple2))

myTupleNumber = (23,4,453,5,45)
myTupleString = ('Timur', 'Hello', 'house', 'Water')
myTupleMixed = (23.23, 's', 'some word')

myText = 'I am learning Python'
myTextList = list(myText)
print(myTextList)

word = 'Python'
myTupleChar = tuple(word)
print(myTupleChar)

myListNumber = list(range(1,11))
print(myListNumber)
myListNumber.append(15)
print(myListNumber)

myTupleNumber = tuple(myListNumber)
print(myTupleNumber)

myTupleNumber = (23,4,453,5,45)
myTupleString =  ('Timur', 'Hello', 'house', 'Water')
myTupleMixed = (23.23, 's', 'some word')

print(myTupleNumber[2])
print(myTupleNumber[:3])
myListFrom_tuple = list(myTupleNumber)
print(myListFrom_tuple)

nameUser, greeting, buildingType, drink = myTupleString
print(nameUser)

someList = (1.3, 45, 'Something', 32)
percentage, someNumber, someWord, age = someList
print(someWord)

someFloatNum, someNumber2, someT, someN = someList
print(someFloatNum)

name2 = 'Aiperi'
someName2 = 'Adilet'

name2, someName2 = someName2, name2
print(nameUser)

myTupleNumber = (23,4,453,5,45)
myTupleString =  ('Timur', 'Hello', 'house', 'Water')
myTupleMixed = (23.23, 's', 'some word')

i = 0
while i < len(myTupleString):
    print(myTupleString[i])
    i += 1

for word in myTupleString:
    print(word, end=' ')

myNestedTuple = (
    (34,243,4),
    (324,54,6)
)

for row in myNestedTuple:
    for number in row:
        print(number)

# set
mySet = {}
mySet2 = set()

someList = [12,34,54,6,12,34]
print(someList)

mySet3 = {12,34,54,6,12,34}
print(type(mySet3))

mySet3.add(45)
print(mySet3)

someList2 = (123,45,56,67)
someList2 = list(set(someList2))
print(someList2)

print(mySet3)
mySet3.remove(34)
print(mySet3)

mySet3.discard(12)
print(mySet3)

for i in mySet3:
    print(i, end=" ")

hospital1 = set()
command = ' '
print('\n')
while command !='no':
    hospital1.add(input('Name of  the doctor: '))

    command = input('Continue?')
    if command == 'no':
        print(hospital1)

hospital2 = set()
command = ''
print('\nSecond set ')
while command != 'no':
    hospital2.add(input('Doctor name?'))

    command = input('Continue?')
    if command == 'no':
        print(hospital2)


