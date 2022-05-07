myList = [23,43,54,34,54,56]

for i in myList:
    print(i, end='\n')

print("*"*20)
iterList = iter(myList)
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))

class StopIterClass:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter +=1
            return 1
        else:
            raise StopIteration

myIterObj = StopIterClass(10)
print(next(myIterObj))
print(next(myIterObj))

print("*"*20)

def gen_function():
    for i in myList:
        yield i

for item in gen_function():
    print(item)

print("*"*20)

word = "I am learning programming"
iterWord = iter(word)
print(next(iterWord))
print(next(iterWord))
print(next(iterWord))
print(next(iterWord))
print(next(iterWord))
print(next(iterWord))
print(next(iterWord))
print(next(iterWord))

print("*"*20)

def iter_function():
    for i in word:
        yield i

for letter in iter_function():
    print(letter)

with open('myText.txt', 'w') as myfile:
    myfile.write("""Объект, элементы которого будем перебирать.
Необязательно это должен быть список,
это может быть, например,множество или словарь.
    """)

with open('myText.txt', 'r') as rfile:
    line1 = rfile.readlines()

def line_function():
    for i in line1:
        yield i

for line in line_function():
    print(line)


