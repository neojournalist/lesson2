class Teacher:
    def __init__(self, name, exp, subject, students):
        self.__nameTeacher = name
        self.__experience = exp
        self.__subjectTeacher = subject
        self.__studentsNumb = students

    def displayInfo(self):
        print(f'Teacher name: {self.__nameTeacher}'
              f'\nExperience: {self.__experience}'
              f'\nSubjects: {self.__subjectTeacher}'
              f'\nStudents: {self.__studentsNumb}')



class MathTeacher(Teacher):
    def __init__(self, name, exp, subject, students, number1, number2, number3):
        Teacher.__init__(self, name, exp, subject, students)
        self.numb1 = number1
        self.numb2 = number2
        self.numb3 = number3

    def findAvg(self):
        result = (self.numb1 + self.numb2 + self.numb3) / 3
        print(f'the average number is {result}')




class GeographyTeacher(Teacher):
    def __init__(self, name, exp, subject, students, country):
        Teacher.__init__(self, name, exp, subject, students)
        self.countryG = country

    def findCapital(self):
        if self.countryG == 'Japan':
            print('Capital city is Tokyo')
        else:
            print('Not defined')

class DrawingTeacher(Teacher):
    def __init__(self, name, exp, subject, students, figure):
        Teacher.__init__(self, name, exp, subject, students)
        self.figureD = figure

    def findSimilarObj(self):
        if self.figureD == 'round':
            print('Planets have round form')
        elif self.figureD == 'triangle':
            print('Pyramids in Egypt are triangular form')
        elif self.figureD == 'square':
            print('Books are in square form')

class MathGeogTeacher(Teacher, MathTeacher, GeographyTeacher):
    def __init__(self, name, exp, subject, students, country, number1, number2, number3):
        Teacher.__init__(self, name, exp, subject, students)
        MathTeacher.__init__(self, number1, number2, number3)
        GeographyTeacher.__init__(self, country)

    def introducing(self):
        print(f'My name is {self.__nameTeacher} and I teach Math and Geography')





