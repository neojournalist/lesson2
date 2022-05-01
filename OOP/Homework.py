class Person:
    def __init__(self, name, age, address):
        self.__namePerson = name
        self.__agePerson = age
        self.__addressPerson = address
        self.__can_vote = 'Yes'

    def getAge(self):
        return self.__agePerson

    def setAge(self, newAge):
        self.__agePerson = newAge
        if newAge >= 18:
            self.__can_vote = 'Yes'
        else:
            self.__addressPerson = 'No'

    def getVote(self):
        return self.__can_vote

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
        self.__bankId = str(newID)

    def setBalance(self, finBalance):
        self.__bankBalance = int(finBalance)


    def deposit(self, number):
        newBalance = int(finBalance) + int(number)
        print(f'Вы пополнили счет {id} на сумму: {number}'
              f'Баланс после пополнения счета: {newBalance}')

    def withdraw(self, amount):
        newBalanceWithdraw = int(finBalance) - int(amount)
        if finBalance > 0:
            print(f'Вы сняли со счета {id} : {amount}'
                f'Баланс после снятия со счета: {newBalanceWithdraw}')
        else:
            print('У вас закончились деньги на балансе')

    def displayInfo(self):
        print(f'Текущий баланс: {finBalance} сом')








def main():
    person1 = Person('Tina', 23, 'Mira 4')
    person1.displayInfo()

    user1 = BankAccount('12373494954', 350)
    user1.displayInfo()


if __name__ == '__main__':
    main()









