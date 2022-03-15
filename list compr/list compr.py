newList = [i**2 for i in range(1,11)]
print(newList)

myText = 'I love programming so much and I would like to improve my skills'
myList = [i for i in myText]
print(myList)

userWord = (input('Enter any word: '))
userCheck = [i for i in userWord if i not in ['a', 'e', 'i', 'o', 'u']]
print(userCheck)

list1 = [2,3,4,5]
list2 = [20,41,28,56]
newList2 = [ 'True'  if b % a ==0 else 'False' for a,b in zip(list1, list2)]
print(newList2)