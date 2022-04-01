age = int(input('Age: '))

print(age)

print()
try:
    age = int(input('Age: '))
    print(age)

except:

number1 = 0
number2 = 0

result = 0
try:
    number1 = int(input('Number1: '))
    number2 = int(input('Number2: '))
    result = number1/number2
except ZeroDivisionError as ze:
    print('Вы пытались делить на ноль!')
except ValueError as ve:
    print('Вы ыыкли строковое значение!')
except:
    print('Other mistake!')
finally:
    print(result)

listPeople = ['Adam', 'Peter', 'Stepan', 'Alena']

try:
    numberIndex = int(input('Enter index number: '))
    print(listPeople[numberIndex])

except IndexError as ie:
    print('Вы ввели больше положенного индекса!')

print(listPeople)