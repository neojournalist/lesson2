myList = list(range(1,20))
print(myList)

newList = []

for i in myList:
    newList.append(i + 5)

newList2 = [i + 5 for i in myList]
print(newList2)

word = 'some word'

newList2 = [word for i in range(3)]
print(newList)

newList3 = []
for i in range(3):
    newList3.append(word)

numbers = [12,343,11,17,54,34,54,15,21,12,54,12]

#i % 2 == 0
newEvenNumbers = [i for i in numbers if i % 2 == 0]
print(newEvenNumbers)

newEvenNumbers2 = [i if i % 2 == 0 else 'not even' for i in numbers]
print(newEvenNumbers2)
#3list2 = [123, 34,23,5]
#list3 = [2,34,4,5]

# Set and Dictionary
mySet = {i * 2 for i in numbers}
print(mySet)

myDict = {i: i +10 for i in range(1,20,2)}
print(myDict)

name = input('Enter your name: ')
nameList = [name for i in range(10)]
print(nameList)

newList4 = [18, 43, 9, 65, 12, 65, 24, 6]
listNew = [i / 3 for i in newList4]
print(listNew)

listNew2 = [i for i in newList4 if i % 3 == 0]
print(listNew2)

#cityList = []
#for i in range(5):
#    cityList.append(input('City: '))

#newCities = ['matching' if 'Tokyo' == i else 'Not matching' for i in cityList]
#print(newCities)

# ZIP method
list2 = [123, 34,23,5]
list3 = [2,3,4,5]
newList5 = [num1 * num2 for num1, num2 in zip(list2, list3)]
print(newList5)

for a, b in zip(list2, list3):
    print(a * b)
#myNumbers = [1,34,5,4]
#num1, num2, num3, num4 = myNumbers #unpacking

userNumb = (input('Enter a number: '))
newUserNumb = [i * 3 and i + 10 for i in range(10)]
print(newUserNumb)


