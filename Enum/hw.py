num = input('Enter a number to calculate power of two: ')

newList = range(0, int(num))
newList2 = []
counter = 1

for i in newList:
    if i < int(num):
        print(f'{i ** 2}')
print(f'Sum is {sum(newList)}\n'
      f'Avg is {sum(newList)/len(newList)}')
             # f'Avg is {}')


