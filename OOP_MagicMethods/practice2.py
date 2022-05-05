class Area:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def findArea(self):
        return self.height * self.width

    def __lt__(self, other):
        if isinstance(other, Area):
            return self.findArea() < other.findArea()

        return False

    def __gt__(self, other):
        if isinstance(other, Area):
            return self.findArea() > other.findArea()
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Area):
            return self.findArea() == other.findArea()
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Area):
            return self.findArea() <= other.findArea()
        else:
            return False


    def __ge__(self, other):
        if isinstance(other, Area):
            return self.findArea() >= other.findArea()
        else:
            return False

    def __call__(self, a, b):
        return self.height * self.width + a + b

    def __mod__(self, other):
        if isinstance(other, Area):
            return self.height * self.width % other
        else:
            return self.height * self.width % other

    def __pow__(self, power, modulo=None):
        return self.height * self.width ** power

    def __contains__(self, item):
        listOfSides = [self.width, self.height]

        if item in listOfSides:
            return True
        return False

    def __getitem__(self, item):
        listOfSides = [self.height, self.width]

        return listOfSides[item]


def main():
    area1 = Area(12,30) #360
    area2 = Area(15,20) #300

    print(area1 > area2)
    print(area1 < area2)
    print(area1 == area2)
    print(area1 >= area2)
    print(area1 <= area2)

    print(area1 % 4)
    print(area2 % 6)

    print(area1 ** 2)
    print(area1(2,3))

    print(21 in area1)




if __name__ == '__main__':
    main()