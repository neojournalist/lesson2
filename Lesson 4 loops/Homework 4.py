name = input('Enter your name: ')

print(f'{name * 20}')

counter = 1

while counter <= 25:
    print(counter*5)
    counter += 3

counter2 = int(input('Enter a number: '))

while counter2 > 0:
    print('The result number +10: ', counter2 + 10)
    counter2 = int(input('Enter a number: '))
    if counter2 == 0:
        print('Not defined')

word = input('Enter a word:')

for i in word:
    print(f'{i*2}', end="")