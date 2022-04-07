import random
#from random import random, randint
from random import *
from copy import deepcopy
from math import *
from decimal import decimal

#random num between 0.0 to 1.0
randomPercentage = random() * 100
#randomPercentage = random() * 100
print(randomPercentage)

#random number between 20 and 50
randNum = randint(20,51)
print(randNum)

randNum2 = randint(1000,3000)
print(randNum2)

#randrange
randNumRange = randrange(0,100,5)
print(randNumRange)

result = 10 + randNumRange
print(result)

#choice, shuffle
listNum = [i for i in range(1,21)]
print(listNum)

choiceRandNum = choice(listNum)
print(choiceRandNum)

listPeople = list()

counter = 1
for i in range(10):
    print(f'Enter name for {counter} :')
    listPeople.append(input('Enter name: '))
    counter +=1

priceWon = choice(listPeople)
print(f'Winner is: {priceWon}')

#shuffle
shuffle(listNum)
print(listNum)

shuffList = list()

listNum1 = [12,32,3]
listNum2 = listNum1
listNum3 = deepcopy(listNum1)

#listNum1[2] = 12
listNum3[2] = 12

newShuffleList = deepcopy(listNum)

shuffle(newShuffleList)
print(newShuffleList)

#MATH
num1 = 5
print(5**2)
print(pow(5,2))

num2 = 144
print(sqrt(num2))

num3 = 23.344444534
print(ceil(num3))
print(floor(num3))

num4 = 10
print(log(10,3))

num5 = 25
print(log2(num5))

num3 = 23.563434
print(round(num3))

num3 = Decimal('0.1')
num3 += 23.435243

print(num3)
