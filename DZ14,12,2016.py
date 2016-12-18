from check_disk import find, summa

def menu():
    """функция выводит меню, принимает выбор пользователя, и возвращает выбор"""
    choise = None
    while choise not in range(0, 3):
        try:
            choise = int(input('''\t\t\tЭто меню управления программой.
            Что-бы посчитать сумму файлов в дирректории, выберете "1"
            Что-бы выполнить поиск файлов в дирректории по фильтру, выберете "2"
            Что-бы выйти из программы выберете "0"\n'''))
        except:
            continue
    return choise

def main():
    choise = None
    print('Здравствуйте, эта программа поможет вам найти сумму фалов в указанной директории, отфильтрует файлы по имени.')
    while choise != 0:
        choise = menu()
        if choise == 1:
            try:
                for a in summa(input('Введите путь до директории в которой нужно посчитать сумму файлов:')):
                    print(a, 'Kb')
            except:
                print('Ошибка!')
        elif choise == 2:
            try:
                for a in find(input('Введите путь до директории:'), input('Введите фильтр по которому будем искать совпадения:')):
                    print(a)
            except:
                print('Ошибка!')
    input('Спасибо за использование нашего П.О. , нажмите Ентер чтобы выйти.')

main()

#
# for a in summa('/home/konstantin'):
#    print(a)
#
# for a in find('/home/konstantin', 'skri'):
#    print(a)
