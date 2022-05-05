class Area:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def findArea(self):
        return self.height * self.width


    def __lt__(self, other):
        if isinstance(other, Area):
            return self.other < other.Area:
        else:
            return False

    def __gt__(self, other):
        if self.square > other.sqaure:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.square == other.sqaure:
            print()
        else:
            return False

def main():
    f1 = Area(5, 4)
    f2 = Area(3, 5)
    print(f1.findArea())
    print(f2.findArea())


    print(f1 > 10)


if __name__ == '__main__':
    main()
