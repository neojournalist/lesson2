#open, close, read, write
#r - read files
#w - write files
#a - add files

#myFile = open('info.txt','w')
#myFile.close()

try:
    myFile = open('info2.txt', 'r')

    try:
        print('Hello the file doing well')
    except:
        print('Some error')
    finally:
        myFile.close()

except FileNotFoundError:
    print('Not able to process the file')

print('code....')

with open('info.txt', 'r') as myfile:
    print('Hello file is doing well')

with open('info2.txt', 'w') as myfile2:
    myfile2.write("""Heellloo I am learning Python this morning
    """)

infoUser = input('Input your text: ')

with open('info3.txt', 'w') as myfile3:
    myfile3.write(infoUser)

with open('info2.txt', 'a') as myfile4:
    myfile4.write('Updating')

with open('info2.txt', 'r') as rfile:
    line1 = rfile.readline()
    line2 = rfile.readline()
    textfile = rfile.read()
print(line1)
print(line2)
print(textfile)

someText = " "
with open('info2.txt', 'r') as rfile:
    for line in rfile:
        someText += line
print(someText)

with open('info2.txt', 'r') as rfile:
    line = rfile.readline()

    while line:
        print(line, end = " ")
        line = rfile.readline()

    with open('info2.txt', 'r') as rfile3:
        contents = rfile3.readlines()

    print(contents)
    line1 = contents[0]
    print(line1)
    line3 = conents[2]
    print(line3)



