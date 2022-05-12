def print_text(func):
    def text1():
        print('***********')
        print(func())
        print('***********')
    return text1

def len_text(func):
    def numb():
        print(len(func()))
    return numb

@print_text
@len_text
def my_text():
    return 'text1'

def main():
#    print(my_text())
    myfunction = my_text()
    print(myfunction())

if __name__ == '__main__':
    main()

def decorator_py(funct):
    def wrapper():
        stringLen = len(funct())
        textFromfunct = funct()

        print("******")
        print(textFromfunct)
        print(stringLen)
        print("******")
    return wrapper

def decorator_py2(funct):
    def wrapper():
        stringLen = len(funct())
        print(stringLen)
    return wrapper

@decorator_py
def my_text():
    return 'sdadsaasd'

def main():
    my_text()

if __name__ == '__main__':
    my_text()
