class Car:
    def __init__(self, modelYear, carBrand, carModel, carFuel):
        self.__year = modelYear
        self.__brand = carBrand
        self.__model = carModel
        self.__fueltype = carFuel
        self.__condition = None

    def setYear(self, newYear):
        self.__year = newYear
        if newYear > 2010:
            self.__condition = 'New Car'
        else:
            self.__condition = 'Old Car'

    def setBrand(self, newBrand):
        self.__brand = newBrand

    def setModel(self, newModel):
        self.__model = newModel

    def setFuelT(self, newFuel):
        self.__fueltype = newFuel

    def get_condition(self):
        return self.__condition

    def displayInfo(self):
        print("Information about this car"
        "\n Year: {0}"
        "\n Brand: {1} "
        "\n Model: {2} "
        "\n Fuel type: {3}".format(self.__year, self.__brand, self.__model, self.__fueltype))

def main():
    car1 = Car(2000, 'Tesla', 'Model S', 'electro')
    car1.displayInfo()
    car1.setYear(2000)
    print(car1.get_condition())




if __name__ == '__main__':
    main()







