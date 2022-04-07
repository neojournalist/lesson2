listWorker = ['Asel', 'Marat', 'Peter', 'Lisa']

def showWorkers(listWorkers):
    for w in listWorker:
        print(w, end=" ")

    print(f'\nNumber of workers: {len(listWorkers)}')

def main():
    listWorker = ['Asel', 'Marat', 'Peter', 'Lisa']
    showWorkers(listWorker)

if __name__ == '__main__':
    main()
