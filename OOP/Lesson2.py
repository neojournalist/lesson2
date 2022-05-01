from datetime import *

class AirConditioner:
    def __init__(self, modelName):
        self.nameModel = modelName
        self.temper = None
        self.timeNow = datetime.now().time()

    def displayInfo(self):
        print(f' Информация. \n'
              f' Model {self.nameModel}'
              f'\n Current Temp {self.temper}'
              f' \n Time {self.timeNow}'
              f'\n *****************')

    def turnedOff(self):
        print(f' AirCon is turned off')
        self.temper = None
        self.timeNow = None

    def turnedOn(self):
        print(f'AirCon is turned on')
        self.temper = 20
        self.timeNow = datetime.now().time()

    def changeTemp(self, temperature):
        self.temper = temperature
        print(f'New temp: {self.temper}')

    def makeHot(self):
        self.temper = 35
        print(f'New temp: {self.temper}'
              f'\n Make it hot')

class Person:
    def __init__(self, name):
        self.__namePerson = None
        self.__agePerson = 20

    def set_age(self, newAge):
        if 1 < newAge < 100:
            self.__agePerson = newAge
        else:
            print('Age does not exist')

    @property
    def name(self):
        return self.__namePerson

    def getAge(self):
        return self.__agePerson

    @name.setter
    def name(self, newName):
        self.__namePerson = newName.capitalize()

    def displayInfo(self):
        print("""
        Info about this person
        Name: {0}
        Age: {1}
        """.format(self.__namePerson, self.__agePerson))



airCond_1 = AirConditioner('Samsung tx54')
airCond_2 = AirConditioner('LG')
airCond_3 = AirConditioner('Beko')

airCond_1.displayInfo()
airCond_1.turnedOn()
airCond_1.displayInfo()

airCond_2.turnedOn()
airCond_2.makeHot()
airCond_2.displayInfo()

airCond_3.turnedOff()
airCond_3.displayInfo()

print(airCond_1.temper)
airCond_1.temper = 26
print(airCond_1.temper)

person1 = Person('Adilet')
person2 = Person('Samat')

#print(person1.getName())
#person1.setName('askar')

#print(person1.getName())
print(person1.getAge())
person1.set_age(15)
print(person1.getAge())

print(person1.name)
person1.name= 'Samat'

print(person1.name)

"""
1) Создать класс Автомобиль - Car. С приватными полями год выпуска, бренд, модель, тип топлива, состояние
• Создать конструктор для принятия значений
• Создать get и set методы для доступа к этим значениям
• Если год выпуска автомобиля старее 2010 года, установить значение
состояние как ‘’old’’ иначе ‘’new’’
• Создать метод для отображения
• В главном методе создать 3 объекта с разными значениями и вызвать
метод для отображения всех значений
"""

