num1 = None
num2 = None
result = None

try:
    num1 = int(input('Num1: '))
    num2 = int(input('Num2: '))

    if num1 <= 0:
        raise Exception('First num should be bigger than 0!')
    elif num2 <=0:
        raise Exception('Second num should be bigger than 0!')
    result = num1 / num2

except ValueError:
    print('enter number')
except TypeError:
    print('Mistake')
except ZeroDivisionError:
    print('Cannot do!')
except Exception as e:
    print(f'You made a mistake {e}')
finally:
    print(f'Result: {result}')

finally:
    result = num1/num2

    try:
        result = num1/num2

        except
