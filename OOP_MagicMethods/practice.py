class Car:
    def __init__(self, year, volume, model):
        self.year = year
        self.volume = volume
        self.model = model

    def __str__(self):
        return f' My model car is {self.year} and {self.model}'

    def __add__(self, other):
        if isinstance(other, Car):
            return self.volume + other.volume
        return self.volume + other

    def __sub__(self, other):
        if isinstance(other, Car):
            return self.volume - other.volume
        return self.volume - other



def main():
    car1 = Car(1989, 2.5, 'Audi100')
    car2 = Car(2000, 3.6, 'MercedesS')

    print(car1)
    print(car2)
    print(car1 + car2)
    print(car2 - car1)




if __name__ == '__main__':
    main()