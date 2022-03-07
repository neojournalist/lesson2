set1 = {10, 20, 30, 40, 50}
set2 = {10, 20, 30}
set3 = set1.difference(set2)
print(set3)

set4 = {10, 20, 30, 40, 50}
set5 = {60, 70, 80, 90, 10}
set6 = set4.intersection(set5)
print('Два множества имеют общий элемент и это: ', set6)

set4 = {10, 20, 30, 40, 50}
set5 = {60, 70, 80, 90, 10}
print(set4 - set5)
