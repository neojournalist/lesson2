def hello():
    print('Hello world')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def display(self):
        print(f'Name:{self.name}'
              f'\nAge:{self.age}')

    def addAge(self, someNum):
        self.age = self.age + someNum


 #   def __add__(self, other):
#$       if isinstance(other, Person):
 #           return self.age + other.age
 #       elif isinstance(other, (int, float):
 #           return other + self.age


    def __iadd__(self, other):
        self.age = self.age + other
        return self.age

    def __radd__(self, other):
        return self.age + other

    def __sub__(self, other):
        return self.age - other

    def __rsub__(self, other):
        return self.age - other

    def __mul__(self, other):
        return self.age * other

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.age == other.age:
            print('Equal')
        else:
            print('Not equal')

    def __len__(self):
        return len(self.name)

    def __truediv__(self, other):
        if isinstance(other, Person):
            return self.age/other.age

        return self.age/other

    def __rtruediv__(self, other):
        return self.age/other

#    def __contains__(self, item):





def main():
    hello()

    p1 = Person('Samat', 25)
    p2 = Person('Adilet', 21)
    p3 = Person('Timur', 28)

    p1.display()

#    print(p1 + 10)
    print(p1 -2)
    print(p1 * 2)


#    resultAgeTwo = p1 + p2
#    print(resultAgeTwo)

    result3 = 10 + p1
    print(result3)

    print(p1 > p2)

    print(p1/4)




if __name__ == '__main__':
    main()