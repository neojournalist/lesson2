"""
class animal
three parameters - age , type(aatribute)
sound of an animal
breed

create a function inside Animal class that displays all the info
"""
class Animal:
    def __init__(self, typeAnimal, age, sound):
        self.typeAnimal = typeAnimal
        self.age = age
        self.sound = sound

    def animalInfo(self):
        print(f'{self.typeAnimal} is {self.age} years old. And it makes this sound {self.sound}.')

cow = Animal('cow', 3, 'Mu-Mu')
cow.animalInfo()

cat = Animal('cat', 2, 'Miu miu')
cat.animalInfo()

dog = Animal('dog', 6, 'gav gav')
dog.animalInfo()