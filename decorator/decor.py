def bread(funct):
    def wrapper():
        print('`~~~~`')
        funct()
        print('~~~~')
    return wrapper

def tomatoes(funct):
    def wrapper():
        print('@~@~')
        funct()
        print('@~@~')
    return wrapper

def cucumber(funct):
    def wrapper():
        print('&&&&')
        funct()
        print('&&&&')
    return wrapper





@bread
@tomatoes
@cucumber
def meat():
    print('=Meat=')


def main():
    meat()

if __name__ == '__main__':
    main()