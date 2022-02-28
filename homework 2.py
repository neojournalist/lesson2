greeting = input('Please enter your greeting: ')
print(greeting[::-1])

course = ('I am learning Python Django')
print('Course name:', course[14:])

word1 = '$$$Python@@@'
word2 = '%%%Programming'
word3 = 'City&&&'
word4 = '****Computer***'

print(word1[3:9], '\n', word2[3:], '\n', word3[:4], '\n', word4[4:12])

number = input('Your favourite number: ')
colour = input('Your favourite colour: ')
city = input('Your favourite city: ')
food = input('Your favourite food: ')

print('{0} {1} {2} {3}'.format(number, colour, city, food))
print(f"Personal favourites {number} , {colour}, {city}, {food}.")