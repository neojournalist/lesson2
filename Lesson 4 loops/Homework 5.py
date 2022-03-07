import statistics

for i in list(range (15,101,5)):
    print(i, end=" ")


cities = ['Moscow', 'Bishkek', 'NY', 'Tashkent', 'Almaty', 'Talas', 'NY', 'Moscow']
setCity = set(cities)
print(setCity)

myList = [34, 31, 5, 53,1,34, 5]
average = statistics.mean(myList)
print(average)

mySum = sum(myList)
print(mySum)

myList2 = ['Елена', 'Степан', 'Мурат', 'Асан', 'Айсулуу']

for i in myList2:
    if i != 'Степан':
        print(i, 'получает зп: 50 тыс рублей', '\n')
    else:
        print(i, 'получает зп: 70 тыс рублей', '\n')

myList3 = ['Елена', 'Степан', 'Мурат', 'Асан', 'Айсулуу']
question = input('Какое имя желаете удалить: ')

if question in myList3:
    myList3.remove(question)
    print('Новый список после удаления: ', myList3)
    question2 = input('Хотите продолжить: ')
    if question2 != 'нет':
        question
        if question in myList3:
            myList3.remove(question)
            print('Новый список после удаления: ', myList3)
            question2 = input('Хотите продолжить: ')
    else:
        print('Программе завершена')








