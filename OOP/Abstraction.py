from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, nameFigure, color):
        self.name = nameFigure
        self.colorFigure = color

    @abstractmethod
    def find_square(self):
        pass

class Square(Figure):
    def __init__(self, nameFigure, color, height, width):
        super().__init__(nameFigure, color)
        self.heightSquare = height
        self.widthSquare = width

    def find_square(self):
        square = self.heightSquare * self.widthSquare
        return square

class Circle(Figure):
    def __init__(self, nameFigure, color, radius):
        super().__init__(nameFigure, color)
        self.radius = radius

    def find_square(self):
        result = pi * pow(self.radius, 2)
        return result

class Triangle(Figure):
    def __init__(self, nameFigure, color, a, h):
        super().__init__(nameFigure, color)
        self.hei = h
        self.a = a

    def find_square(self):
        result = 0.5 * self.a * self.hei
        return result




def main():
    fig1 = Square('square', 'black', 4, 5)
    squareofFig1 = fig1.find_square()

    fig2 = Circle('Round', 'red', 12)
    squareofFig2 = fig2.find_square()

    fig3 = Triangle('pyramid', 'green', 5, 7)
    suqareofFig3 = fig3.find_square()

    print(f'Square of Fig1 is {squareofFig1}')
    print(f'Square of Fig1 is {squareofFig2}')
    print(f'Square of Fig1 is {squareofFig3}')

if __name__ == '__main__':
    main()