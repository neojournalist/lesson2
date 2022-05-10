

numb = input('enter number: ')
    def my_genFindPower(numb):
        for i in range(1, numb+1):
            yield i**2

findPower = my_genFindPower(numb)
sumNumbs = 0
for numb in findPower:
    print(numb)
    sumNumbs += numb

avgNumb = sumNumbs/numb

print(f'Sum is {sumNumbs}\n'
      f'Avg is {avgNumb}')




