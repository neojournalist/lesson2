import openpyxl
from openpyxl import *

wb = load_workbook('/Users/altynai/Downloads/food.xlsx')
sheet = wb.worksheets[0]
print('Success!')

for column in sheet['A']:
    print(column.value)

f19 = sheet['F19'].value
print(f19)

cells = sheet['A18':'H18']
cellsdata = cells[0]

print(cells)
print(cellsdata)

#for info in cellsdata:
