#creating lambda functions
def helloSay():
    print('Hello my dear friend!')

def helloSay2(name):
    print(f'Hello {name}')

def addNumsThree(num1, num2, num3):
    return num1 + num2 + num3

def mathOperation(n1, n2, n3, operation):
    result = operation(n1, n2, n3)

    return result

def main():
    sayHello = lambda: print('Hello my dear friend!')

    sayHello()

    helloSay()

    sayHello2 = lambda name: print(f'Hello {name}')
    sayHello2('Samat')

    addThreeNums = lambda n1,n2,n3: n1 + n2 + n3
    print(addThreeNums(34,54,65))

    result = 100 + addThreeNums(34,54,65)

    print(addNumsThree(34, 56, 65))

    findAvg = lambda listMy: sum(listMy)/len(listMy)
    print(findAvg([23, 45, 56, 67]))

    #1 Finding average among three numbers
    avgResult = mathOperation(12, 43, 54, lambda num1, num2, num3:(num1 + num2 + num3)/3)
    print(avgResult)

    sumThreeNums = mathOperation(34, 435, 65, addThreeNums)
    print(sumThreeNums)

    multiplyResult = mathOperation(23, 45, 54, lambda num1, num2, num3: num1 * num2 * num3)
    print(multiplyResult)

if __name__ == '__main__':
    main()