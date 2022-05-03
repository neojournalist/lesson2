from abc import ABC, abstractmethod


class Bank:
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def getBalance(self):
        pass

class BankA(Bank):
    def __init__(self, balance):
        super().__init__(balance)

    def getBalance(self):
        return self.balance

class BankB(Bank):
    def __init__(self, balance):
        super().__init__(balance)

    def getBalance(self):
        return self.balance

class BankC(Bank):
    def __init__(self, balance):
        super().__init__(balance)

    def getBalance(self):
        return self.balance



class Car:
    def __init__(self, model, color, maxSpeed):
        self.mod = model
        self.col = color
        self.speedMax = maxSpeed

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def gas(self):
        pass

class Sedan(Car):
    def __init__(self, model, color, maxSpeed):
        super().__init__(model, color, maxSpeed)

    def brake(self):
        return 'two'

    def gas(self):
        return 40



class SportCar(Car):
    def __init__(self, model, color, maxSpeed):
        super().__init__(model, color, maxSpeed)

    def brake(self):
        return 'two'

    def gas(self):
        return 80


class FamilyCar(Car):
    def __init__(self, model, color, maxSpeed):
        super().__init__(model, color, maxSpeed)

    def brake(self):
        return 'four'

    def gas(self):
        return 30


def main():
    b1 = BankA(100)
    b2 = BankB(150)
    b3 = BankC(200)

    print(b1.getBalance())
    print(b2.getBalance())
    print(b3.getBalance())

    c1 = Sedan('audi', 'white', 200)
    c2 = SportCar('ferrari', 'red', 350)
    c3 = FamilyCar('toyota', 'grey', 120)

    print(c1.gas())
    print(c1.brake())
    print(c2.gas())
    print(c3.gas())







if __name__ == '__main__':
    main()



