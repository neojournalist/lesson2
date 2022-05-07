listNames = ['AM', 'KM', 'PL']

counter = 1
for name in listNames:
    print(f'{counter}.{name}')

print('*'*20)

for elem in enumerate(listNames):
    print(f'{elem[0]+1}.{elem[1]}')

listNumber = [21, 34, 54]

n1, n2, n3 = listNumber
print(n1)

for counter, name in enumerate(listNames):
    print(f'{counter + 1}.{name}', end="\n")

print('*'*20)

for elem in enumerate(listNames, 1):
    print(f'{elem[0]}.{elem[1]}')

word = "programming"

for elem, letter in enumerate(word, 1):
    print(f'{elem}-th letter: "{letter}"')

print('*'*20)


#for counter, name in enumerate(listNames, 1):
 #   listNames[counter] = f'{counter +1} th worker: {name}'

myList = [23,43,54,34,54,56]
for n, m in enumerate(myList):
    print( f'Result of {n+1} number multiplication is {m*10}. \n Result of {n+1} number division is {m / 2}')



