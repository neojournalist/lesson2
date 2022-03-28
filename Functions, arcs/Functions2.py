#args Function
def functionarg(*args):
    print(type(args))
    listNums = list(args)
    for i in args:
        print(i, end=" ")

def main():
    functionarg(23, 45, 56)

    someDict ={
        'name': 'Askar',
        'age': 25,
        'address': 'Mira'
    }

    kwargsFunction(name = 'Askar', age = '25', address = 'Mira 7')
    kwargsFunction(**someDict)

    both(23, 45, 56, name = 'Askar', age = '25', address = 'Mira 7')

def both(*args, **kwargs):
    for i in args:
        print(i, end=" ")
    print(args)
    print('=========')
    for k,v in kwargs.items():
        print(f'{k}:{v}')
    print(kwargs)


def kwargsFunction(**kwargs):
    print(type(kwargs))

    for k,v in kwargs.items():
        print(f'{k}:{v}')



if __name__ == '__main__':
    main()
