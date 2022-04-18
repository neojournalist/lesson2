from random import *


"""
1.	Напишите программу на Python для чтения последних n строк файла.
Количество последних строк принять от пользователя.
"""


def printLastLines(filename, n):
    with open(filename, 'r') as file:
        linesFromFile = file.readlines()

    print(linesFromFile[-n:])

    text = ''
    for textLines in linesFromFile[-n:]:
        text += textLines
    # return textLines


def main():
    filename = 'sometext.txt'

    numLines = int(input('Enter number of lines for display: '))

    lastlines = printLastLines(filename, numLines)


    print()

"""
1.	Напишите программу на Python для подсчета 
количества строк в текстовом файле. 
"""

def countLines(filename):
    numLines = 0
    #counter = 0

    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            line = file.readline()
            numLines +=1
    return numLines

"""
3.	Напишите программу на Python 
для чтения случайной строки из файла.
"""

def readRandLines:
    with open(filename, 'r') as file:
        line = file.readline()
        
        randomLine = randint(line)


if __name__ == '__main__':
    main()
