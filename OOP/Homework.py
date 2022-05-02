class Person:
    def __init__(self, name, age, address):
        self.__namePerson = name
        self.__agePerson = age
        self.__addressPerson = address
        self.__can_vote = 'Yes'

        if self.__agePerson >= 18:
            self.__can_vote = True
        else:
            self.__can_vote = False

    def getAge(self):
        return self.__agePerson

    def setAge(self, newAge):

        if newAge >= 18:
            self.__agePerson = newAge
            self.__can_vote = 'Yes'
        else:
            self.__agePerson = newAge
            self.__can_vote = 'No'

    def getVote(self):
        if self.__can_vote == False:
            return 'Too young for voting'
        else:
            return 'Can vote'

    def displayInfo(self):
        print("Information about this person"
              "\n Name: {0}"
              "\n Age: {1} "
              "\n Address: {2} "
              "\n Voting status: {3}".format(self.__namePerson, self.__agePerson, self.__addressPerson, self.__can_vote))

class BankAccount:
    def __init__(self, id, balance):
        self.__bankId = id
        self.__bankBalance = balance

    def setID(self, newID):
        self.__bankId = newID

    def setBalance(self, newBalance):
        self.__bankBalance = newBalance


    def deposit(self, number):
        newBalance = self.__bankBalance + number
        print(f'Вы пополнили счет {self.__bankId} на сумму: {number}'
              f'\nБаланс после пополнения счета: {newBalance}')

    def withdraw(self, amount):
        newBalanceWithdraw = self.__bankBalance - amount
        if newBalanceWithdraw > 0:
            print(f'Вы сняли со счета {self.__bankId} : {amount}'
                f'\nБаланс после снятия со счета: {newBalanceWithdraw}')
        else:
            print('У вас закончились деньги на балансе')

    def displayInfo(self):
        print(f'Текущий баланс: {self.__bankBalance} сом')

class VipAccount(BankAccount):
    def vipServing(self):
        print('First class service')

class PremiumAccount(BankAccount):
    def privileges(self):
        print()

def main():
    person1 = Person('Tina', 23, 'Mira 4')
    person1.displayInfo()

    user1 = BankAccount('12373494954', 350)
    user1.displayInfo()
    user1.deposit(100)
    user1.withdraw(400)


if __name__ == '__main__':
    main()









