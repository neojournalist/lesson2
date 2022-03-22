# return

def findSum(num, num2):
    print(f'Sum of two nums:{num + num2}')

def findMult(num, num2, num3):
    result = num *num2 * num3
    print(f'result: {result}')

def findSum2(num, num2):
    result = num + num2

    return result

def findMult2(num, num2, num3):
    result = num *num2 * num3
    return result

someNum = 10

result2 = findSum2(20,30) + someNum
print(result2)

#myList = list(range(5,10))
#print(print_list(myList))

#newList = list(print_list(myList))
#print(print_list)

def checkAge(age):
    if age >=18:
        return 'Adult'
    else:
        return 'Too young'

resultAge = checkAge(15)
print(resultAge)

def greeting():
    name = input('Enter your name:')
    print(f'Привет {name}, добро пожаловать в нашу программу!')

greeting()

def sumNumb():
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    print(f'The sum is {num1+num2}')

sumNumb()

def calcAvg(num3, num4, num5):
    avg = (num3 + num4 + num5)/3
    print(avg)

calcAvg(2,4,6)

def calcAvg2(number1, number2, number3):
    myList = [number1, number2, number3]
    avgNumb = sum(myList)/len(myList)
    return avgNumb

print(calcAvg2(20,2,3)

def main()
    # визульно отделить обращение функций от создания фунций

if __name__ == '__main__':
    main()



def div(num6,num7, num8 =3):
    result = num6 / num7 / num8
    return result
num6 = int(input('Enter number 1: '))
num7 = int(input('Enter number 2: '))
num8 = 5

print(div(num6, num7))


