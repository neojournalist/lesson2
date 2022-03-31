from datetime import *

newList = [i**2 for i in range(1,10)]
print(newList)

def charCapLetter(c):
    return c.upper()

word = 'hello'

someList = list(map(charCapLetter, word))
print(someList)

newListCapLetter = list(map(lambda c: c.upper(), word))

def even_odd(x):
    if x % 2 == 0:
        return 0
    else:
        return x

elements = [1, 2, 3, 4]
elements_new = list(map(even_odd, elements))
print(elements_new)

def powerThree(n):
    return n**3

someList3 = [3,2,5,8,9,7]
newListPower = list(map(powerThree, someList3))

newListPower2 = list(map(lambda n: n**3, someList3))

def reverseNum(n):
    n = str(n)
    return n[::-1]

print(reverseNum(567))

def someList(*args):
    somelist = list(args)
    for i in args:
        print(i*3)

print(someList(1,2,3))

def checkPosNeg(n1,n2,n3):
    newList = [n1,n2,n3]

    listpositive = []
    listnegative = []
    for i in newList:
        if i > 0:
            listpositive.append(i)
        else:
            listnegative.append(i)

        print(f'Quantity of negative numbers: {len(listnegative)}\n')
        print(f'Quantity of positive numbers: {len(listpositive)}\n')

def checkPN(n4,n5,n6):
    newList2 = [n4,n5,n6]

    counterNegative = 0
    counterPositive = 0
    for i in newList2:
        if i > 0:
            counterPos += 1
        else:
            counterNeg += 1
    print(f'Quantity of negative numbers: {counterNeg}\n')
    print(f'Quantity of positive numbers: {counterPos}\n')

    checkPN(8,-9,-3)
    checkPosNeg(-4,5,6)

# Task 4 practice
"""
Ваша задача написать функцию, которая узнает сколько остается дней до
определенной даты. Для вызова этой функции вам необходимо передать дату,
после которой вам должно вернутся значение в днях сколько остается времени
до этой самой даты.
"""

def checkTimeLeft(someDate):
    nowDate = datetime.now()

    dateFromUser = datetime.strptime(someDate, '%d/%m/%Y')
    timeLeft = dateFromUser - nowDate

    return timeLeft

someDate = input('Please enter date in this format d/m/yyyy: ')
print(checkTimeLeft(someDate))

#Task 5

divTwo = lambda num1, num2: num2/num1
print(divTwo(4,16))

#Task 4
"""
Необходимо создать функцию, которая, принимая в себя какое-нибудь число
возвращает ответ  Четное  или  Не четное  значение. Далее на основе этой
функции необходимо проверить данный список [12,33,45 ,4,54,1,32,11 ,67,88]
используя ранее созданную функцию на  Четность  или  Не четность 
используя map. У вас должен вернуться следующий новый список:
"""

def ev_odd(y):
    if y % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

elements2 = [1, 2, 3, 4, 5]
elements2_new = list(map(ev_odd, elements2))
print(elements2_new)


def smallLetters(*args):
    somelists = list(args)
    return somelists.lower()


somelists = ['HELLO','HOW ARE YOU', 'I AM FINE', 'THANK YOU']
phrase = list(map(somelists, smallLetters))
print(phrase)


