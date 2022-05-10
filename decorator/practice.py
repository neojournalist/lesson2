def bold(someText):
    def screen():
        print('<b>')
        someText()
        print('</b>')
    return screen

def italic(someText):
    def screen():
        print('<i>')
        someText()
        print('</i>')
    return screen

def underline(someText):
    def screen():
        print('<u>')
        someText()
        print('</u>')
    return screen
        
@bold
@italic
@underline
def displayText():
    print('text1')


def main():
    #text1 = input('Enter your text: ')
    displayText()

if __name__ == '__main__':
    main()