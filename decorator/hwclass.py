class FindType:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, *args):
        for i in args:
            if type(i) == int:
                print(f'{i} is integer type')
            elif type(i) == str:
                print(f'{i} is string type')
            elif type(i) == list:
                print(f'{i} is a list')
            else:
                print(f'{i} is undefined')

class FindSumList:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, *args):
        for i in args:
            if type(i) == list:
                print(f'{i} is a list \n'
                      f'the average of the list is {sum(i) / len(i)}')
            else:
                pass

@FindSumList
@FindType
def simpleFunction(*args):
    print(f'Define types for each value: \n {args}')


def main():
    simpleFunction(23, 'hello', 12, 'ELena', [34, 5, 6], {'one': 1})


if __name__ == '__main__':
    main()
