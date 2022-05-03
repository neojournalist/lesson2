from abc import ABC, abstractmethod


class Person:
    def __init__(self, income):
        self.incomePerson = income

    @abstractmethod
    def calculateMyExpenses(self):
        pass

    @abstractmethod
    def whereToEat(self):
        pass

    @abstractmethod
    def earnMoney(self):
        pass

class Student(Person):
    def __init__(self, income, payments, scholarship):
        super().__init__(income)
        self.pay = payments
        self.sco = scholarship

    def calculateMyExpenses(self):
        expenses = self.incomePerson + self.sco - self.pay
        print(f'Your expenses: {expenses}')

    def whereToEat(self):
        food = input('choose a food to eat: ')
        if food == 'burger':
            print('McDonalds')
        else:
            print('At home')

def main():
    student1 = Student(300, 200, 50)
    result = student1.calculateMyExpenses()
    print(result)
    student1.whereToEat()



if __name__ == '__main__':
    main()




