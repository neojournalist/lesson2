import openpyxl
from openpyxl import *

def decor_find_sum(funct):
    def wrapper(someList):
        sumList =  {sum(someList)}
        with open('resultList.txt', 'w') as f:
            f.write('All the elements in the List: ')
            for i in someList:
                f.write(f'{i}\n')

            f.write('__________________\n')
            f.write(f'Sum of the elements is {sumList}\n')
            f.write('__________________\n')
            
            print('Successfull file')
    return wrapper

def mydecor_SaveExcel(funct):
    def wrapper(someList):
        wb = openpyxl.Workbook()
        sheet = wb.active

        dataList = (
            ('Elements', 'Average of elements', 'Sum of elements'),
            (len(someList), sum(someList)/len(someList), sum(someList))
        )

        for row in dataList:
            sheet.append(row)

        wb.save('listExc.xlsx')

        print('Success Excel')

    return wrapper









@mydecor_SaveExcel
@decor_find_sum
def show_list(someList):
    return someList


def main():
    show_list([32, 54, 546, 65])

if __name__ == '__main__':
    main()