myDictionary = {}
myDictionary2 = dict()

contacts = {'Asan': '+99677855678', 'Aigul': '+889765678', 'Timur': '+998667899'}
numberDict = {'One':1, 'Two': 2, 'Three': 3}
workersDict = {123: 'Rinat talgatov', 34223: 'Usen Urmatov', 12334: 'Elena Stepanova', 343: 'Murat Tilenov'}

contacts['Aisuluu'] = '+997668900'
print(contacts)

listNumber = [123, 43, 2345, 655]
listNumber[2] = 56

companyWorkers = {
    'worker1': {
        'name': 'Urmat Rinatova',
        'age': 32,
        'numberChild' : 3,
        'spouse name' : 'Tamara Tilekova',
        'address' : 'Mir 45',
        'salary' : 30000
    },
    'worker2': {
        'name': 'Elena Stepanova',
        'age': 45,
        'numberChild' : 1,
        'spouse name' : 'Rinat Usmanov',
        'address' : 'Mir 56',
        'salary' : 40000
    }
}
print(companyWorkers['worker2']['numberChild'])

neiList = [
    ['Nei1', 'Uriy Stepanov'],
    ['Nei2', 'Tamara Mar'],
]
neiDict = dict(neiList)
print(type(neiDict))

cars_tuple = (
    ('Ferrari', 150000),
    ('Audi', 20000),
    ('Lexus', 250000)
)

cars_dict = dict(cars_tuple)
print(cars_dict)

companyWorkers = {
    'worker1': {
        'name': 'Urmat Rinatova',
        'age': 32,
        'numberChild' : 3,
        'spouse name' : 'Tamara Tilekova',
        'address' : 'Mir 45',
        'salary' : 30000
    },
    'worker2': {
        'name': 'Elena Stepanova',
        'age': 45,
        'numberChild' : 1,
        'spouse name' : 'Rinat Usmanov',
        'address' : 'Mir 56',
        'salary' : 40000
    }
}

companyWorkers['worker4'] = {'name' : 'Sergei Stepanov'}
companyWorkers['worker4']['age'] = 23
print(companyWorkers)

print(contacts.get('Timur'))

print('Peter' in contacts)

if 'Peter' in contacts:
    print('He exists')
else:
    print('does not exist')

#clean the element
contacts['Aisuluu'] = ' '

del contacts['Aisuluu']
contacts.pop('David')

contacts.update(contacts)
print(contacts)

numberDict2 = ('Three':3, 'Four':4)