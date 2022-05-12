def my_decor(funct):
    def wrapper(arg1, arg2):
        print('Welcome, please introduce yourself: ')
        funct(arg1, arg2)
        print('Nice to meet you {0} your room number is 15'.format(arg1))

    return wrapper

def my_decor_tour(funct):
    def wrapper(arg1, arg2):
        print('We want to have a tour')
        print('{0} I see you paid $1000 for a tour.'
              '\n You are from {1} and you have a discount 10%'.format(arg1,arg2))
    return wrapper


@my_decor
def function_simple(name, city):
    print(f'My name is {name} and i live in {city}')

def main():
    namePerson = input('Name of a person: ')
    city = input('City: ')

    function_simple(namePerson, city)

if __name__ == '__main__':
    main()