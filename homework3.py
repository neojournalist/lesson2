number = int(input('Enter any number: '))

if 2 < number < 9:
    print('The number is bigger than 2 but smaller than 9')
else:
    print('The number is not defined')

weight = int(input('Enter the weight of your package in kilos: '))

if 0 < weight <= 2:
    print(f"You will pay {weight * 3.5} $")
elif 3 <= weight <= 5:
    print(f"You will pay {weight * 5.5} $")
elif 6 <= weight <= 10:
    print(f"You will pay {weight * 7} $")
elif 11 <= weight < 50:
    print(f"You will pay {weight * 10} $")
else:
    print('Your package could not be delivered')