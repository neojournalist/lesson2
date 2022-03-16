students = {
    'student1': {
        'name': 'Anna',
        'age': 15,
        'average grade': 3.5
    },
    'student2': {
        'name': 'Peter',
        'age': 14,
        'average grade': 4.5
    },
    'student3': {
        'name': 'Sara',
        'age': 16,
        'average grade': 4.7
    }
}

for student, data in students.items():
    print(student, ':', data)

keys = ['Hundred', 'Twenty', 'Ten']
values = [100, 20, 10]
new_dict = dict(zip(keys, values))
print(new_dict)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

sampleDict = {
    'class': {
        'student':
            {'name': "Mike", "marks":
                {'physics': 70, "history": 80}
             }
    }
}

for a,b in sampleDict.items():
    for c,d in b.items():
        for e,f in d.items():
            print(f)

print(sampleDict['class']['student']['marks']['history'])