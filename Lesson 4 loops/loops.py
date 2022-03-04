#loops

poem = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
"""

count = 1

while count <= 10:
    print(f'Repeat in {count} \n{poem}')
    count = count + 1

count1 = 10

while count < 15:
    print(count)
    #count = count + 1
    count += 1

i = 1
#while i <= 10:
 #   print(i * 2)
 #   i += 1

range(1,10) #1 - 9

for count in range(1,11):
    print(f'Repear in {count} \n{poem}')

for count4 in range(11):
    print(count4)

counter = 1
while counter <= 15:
    numb = counter ** 3
    print(f'Cubic number of {counter} is {numb}')
    counter += 1

n = int(input('Enter a number for the total sum: '))

currentNumb = 1
totalSum = 0
while currentNumb <= n:
    totalSum = totalSum + currentNumb #totalSum += currentNumb
    currentNumb += 1 #currentNumb = +1

print(totalSum)

n2 = int(input('Enter a number for a total sum: '))
totalSum2 = 0

#range(1,16) 1-15

for currentNumb2 in range(1,n2+1):
    totalSum2 = totalSum2 + currentNumb2

print(totalSum2)

factNumb = int(input('Enter factorial number:'))
i = 1
sumNumb = 1

while(True):
    sumNumb = sumNumb * i
    i += 1

    if i > factNumb:
        break

print(sumNumb)

counter = 1

while counter < 10:
    print(counter)
    counter -= 1
    if counter == 1:
        break

for i in range(11,0,-2):
    print(i)

Counter = 11

while counter >= 1:
    print(counter)
    counter -= 1






