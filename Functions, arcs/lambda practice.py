# lambda practice
def main():
    ageArgs(20, 30, 40)
    nameKwargs(name1= 'Nina', name2='John', name3= 'Mira')

    sqNums = lambda num1: num1**2
    print(sqNums(4))

    avgNums = lambda n1,n2,n3,n4: (n1 + n2 +n3 + n4)/4
    print(avgNums(2,2,2,10))

    num = int(input('Введите сумму для оплаты: '))
    if num in range(1000,2000):
        discountTwo = num - (num * 0.02)
        print(f'Сумма скидки 2% от {num} сом: {discountTwo}')
    elif num in range(2000,5000):
        discountFive = num - (num * 0.05)
        print(f'Сумма скидки 5% от {num} сом: {discountFive}')
    elif num in range(5000,10000):
        discountTen = num - (num * 0.1)
        print(f'Сумма скидки 10% от {num} сом: {discountTen}')
    elif num >= 10000:
        discountTwenty = num - (num * 0.2)
        print(f'Сумма скидки 20% от {num} сом: {discountTwenty}')
    else:
        print(f'Извините, для {num} скидки никакой нет. Купите больше:)')
    print(payment)


def ageArgs(*args):
    listNums = list(args)
    sumAge = sum(args)
    print(sumAge)

def nameKwargs(**kwargs):
    for k,v in kwargs.items():
        print(f'{v}')
    print(kwargs)

def sqNums(num1):
    return sqNums

def avgNums(n1, n2, n3, n4):
    return avgNums

def payment(num):
    return payment


if __name__ == '__main__':
    main()