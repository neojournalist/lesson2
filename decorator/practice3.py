def decorShowAvg(funct):
    def wrapper(someList):
        print('************')
        funct(someList)
        print('************')
        print(f'Average of list is: {sum(someList)/len(someList)}')

    return wrapper

def decorSum(funct):
    def wrapper(someList):
        funct(someList)
        print(f'Sum is {sum(someList)}')

    return wrapper

@decorSum
@decorShowAvg
def show_list(someList):
    print('All the elements in the List: ')
    for i in someList:
        print(i)


def main():
    show_list([32, 54, 546, 65])

if __name__ == '__main__':
    main()