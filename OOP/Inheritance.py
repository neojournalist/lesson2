class Animal:
    def __init__(self, typeanimal, typefood, livingarea):
        self.animalType = typeanimal
        self.foodType = typefood
        self.areaLiving = livingarea

    def sleep(self):
        print(f'{self.animalType} sleeps in {self.areaLiving}')

    def eat(self):
        print(f'{self.animalType} eats {self.foodType}')

class Tiger(Animal):
    def __init__(self, typeanimal, typefood, livingarea, lenght_tail):
        Animal.__init__(self, typeanimal,typefood,livingarea)
        self.tail_l = lenght_tail

    def canHunting(self):
        print('Tiger can hunt and carnivore')

class Monkey(Animal):
    def __init__(self, typeanimal, typefood, livingarea, len_hand, quant_teeth):
        Animal.__init__(self, typeanimal,typefood,livingarea)
        self.len_hand = len_hand
        self.teethQ = quant_teeth


    def canClimb(self):
        print('Monkey can climb trees and eats bananas')

class Mind:
    def __init__(self, typeWord):
        self.wordtype = typeWord

    def canRead(self):
        print(f'It can read {self.wordtype}')

class Parrot(Animal, Mind):
    def __init__(self, typeanimal, typefood, livingarea, typeWord, color):
        Animal.__init__(self, typeanimal, typefood, livingarea)
        Mind.__init__(self, typeWord)
        self.colorAnimal = color


    def canSpeak(self):
        print('Parrots can talk and read')


def main():
    tiger1 = Tiger('Indian tiger', 'meat', 'savanna')
    monkey1 = Monkey('Chimpanzee', 'bananas', 'jungles')

    tiger1.sleep()
    monkey1.sleep()
    parrot1 = Parrot('Ara', 'grains', 'forrest')
    parrot1.canSpeak()
    parrot1.sleep()


if __name__ == '__main__':
    main()