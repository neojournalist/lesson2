def main():
    name = input('Enter your name: ')
    nameRev = lambda n: n[::-1]
    print(nameRev(name))

    findSum = lambda n1: n1 // 10 + n1 % 10
    print(findSum(34))

    printEverySecLetter = lambda w: w[::2]
    print(printEverySecLetter('hello'))

    findAvg = lambda avg: sum(avg)/len(avg)
    print(findAvg([2,3,5]))

    powerN = lambda num1, num2: num1 ** num2
    num1 = int(input('Enter 1 number: '))
    num2 = int(input('Enter 2 number: '))
    print(powerN(num1, num2))

    num3 = int(input('Enter 1 number: '))
    num4 = int(input('Enter 2 number:'))
    if lambda num3, num4: num3 % num4:
        print('Checked!')
    else:
        print('Not working!')






if __name__ == '__main__':
    main()