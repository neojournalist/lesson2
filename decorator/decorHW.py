def decor_find_sum(funct):
    def wrapper(someList):
        funct(someList)
        result = f'Sum of list {sum(someList)}'
        with open('resultList.txt', 'r') as f:
            f.write(result)
        return result

    return wrapper

@decor_find_sum
def show_list(someList):
    print('All the elements in the List: ')
    for i in someList:
        print(i)


def main():
    show_list([32, 54, 546, 65])

if __name__ == '__main__':
    main()