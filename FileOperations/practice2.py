from openpyxl import *
import statistics as stats

wb = load_workbook('/Users/altynai/Downloads/food.xlsx')
sheet = wb.worksheets[0]

cells = sheet['B12':'G28']

for row in cells:
    for data in row:
        print(data.value, end=" ")

cells2 = sheet.iter_rows(min_row=12, max_col=6, max_row=28)

for row in cells2:
    for data in row:
        print(data.value, end=" ")
    print(end="\n")
print('***********')

cells3 = sheet['F19':'G30']
listCells = []

for row in cells3:
    for data in row:
        listCells.append(data.value)

print(f'Median {stats.median(listCells)}')
print(f'Average {stats.mean(listCells)}')
print(f'Variance {stats.variance(listCells)}')
print(f'St Deviation {stats.stdev(listCells)}')

wb2 = Workbook()
sheet2 = wb2.worksheets[0]

regionNames = ['JB', 'Naryn', 'IK', 'Osh', 'Talas']
cityNames = ['ABS', 'Kls', 'Pmn', 'YKL', 'Jnm']
population = [100, 200, 300, 500, 700]
mayorName = ['OL', 'JV', 'GB', 'HY', 'TY']

columnName1 = sheet2.cell(row=1, column=1).value = 'Region'
columnName2 = sheet2.cell(row=1, column=2).value = 'City'
columnName3 = sheet2.cell(row=1, column=3).value = 'Population'
columnName4 = sheet2.cell(row=1, column=4).value = 'Mayor'

counter = 2
for i in range(6):
    sheet2.cell(row = counter, column = 1).value = regionNames[i]
    sheet2.cell(row = counter, column = 2).value = cityNames[i]
    sheet2.cell(row = counter, column = 3).value = population[i]
    sheet2.cell(row = counter, column = 4).value = mayorName[i]
    counter += 1

wb2.save('KGInfo.xlsx')
print('Successfully saved')

