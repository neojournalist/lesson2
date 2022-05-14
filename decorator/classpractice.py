import openpyxl


class TextSum:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, someList):
        sumList = sum(someList)
        with open('resultList2.txt', 'w') as f:
            f.write('All the elements in the List: \n')
            for i in someList:
                f.write(f'{i}\n')

            f.write('__________________\n')
            f.write(f'Sum of the elements is {sumList}\n')
            f.write('__________________\n')

            print('Success')


class SaveExcel:
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, someList):
        wb = openpyxl.Workbook()
        sheet = wb.active

        dataList = (
            ('Elements', 'Average of elements', 'Sum of elements'),
            (len(someList), sum(someList) / len(someList), sum(someList))
        )

        for row in dataList:
            sheet.append(row)

        wb.save('listExc2.xlsx')

        print('Success Excel')

@SaveExcel
def show_list(someList):
    return someList


def main():
    show_list([32, 54, 546, 65])


if __name__ == '__main__':
    main()