class DecoratorBread:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self):
        print('~~~~~~~')
        self.funct()
        print('~~~~~~')

class DecoratorSalad:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self):
        print('@@@@@')
        self.funct()
        print('@@@@@')

class TourDecorator:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, arg1, arg2):
        print('Welcome to our hotel. Please your name?')
        self.funct(arg1, arg2)
        print(f'Nice to meet you Mr. {arg1}')

@DecoratorBread
@DecoratorSalad
def meat():
    print('=Meat=')


@TourDecorator
def func_simple(name, city):
    print(f'My name is {name}. I am from {city}')

@TourDecorator
def func_simple2(name, city, country):
    print(f'My name is {name}. I am from {city} and country {country}')

def main():
    meat()
    func_simple('Askar', 'Berlin')
    func_simple('Askar', 'Berlin', 'Germany')

if __name__ == '__main__':
    main()