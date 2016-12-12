# # Типы данных
#
import pickle
#
# lst = [1, 2, 3, 'qweqwe', {'q': 123}]
# with open('lst.pickle', 'wb') as f:
#     pickle.dump(lst, f)
# f = open('lst.pickle', 'rb')
# lst2 = pickle.load(f)
#
# print(lst == lst2)

# написать функцию добавляющую в БД новый паравоз мощнось, и прю данныею сохр в пикл
# созд функц которая считает все тепловозы в список

sps = {}

def menu():
    """функция выводит меню, принимает выбор пользователя, и возвращает выбор"""
    choise = None
    while choise not in range(0, 5):
        try:
            choise = int(input('''\t\t\tЭто меню управления программой.
            Что-бы просмотреть список тепловозов выберете "1"
            Что-бы добавить тепловоз в список выберете "2"
            Что-бы удалить тепловоз из списка выберете "3"
            Что-бы выйти из программы выберете "0"\n'''))
        except:
            continue
    return choise
def ask(sps = None):
    if sps == None:
        sps = {}
        key = 1
        tep = input('Впишите данные тепловоза через пробел:')
        sps[key] = tep
        return sps
    elif sps != None:
        x = sps.keys()
        y = []
        for i in x:
            y.append(i)
        y.sort()
        key = int(y[-1])
        tep = input('Впишите данные тепловоза через пробел:')
        key += 1
        sps[key] = tep
        return sps
def save(lst_t):
    with open('teplo.pickle', 'wb') as f:
        pickle.dump(lst_t, f)
        f.close()
def read():
    with open('teplo.pickle', 'rb') as f:
        lst_t = pickle.load(f)
        return lst_t
def show(lst_t):
    if len(lst_t) <1:
        print('Список теполвозов пуст, сначала нужно добавить паравоз в список!')
    else:
        for i in lst_t.items():
            print(i)
def dell(lst_t):
    key = int(input('Какой тепловоз вы хотите удалить? введите номер:'))
    if key in lst_t:
        del lst_t[key]
        print('Паравоз', key, 'удален.')
    else:
        print('Выбранного вами тепловоза нет в списке, либо спсок пуст.')
    return lst_t
def main():
    choise = None
    print('\tЗдравствуйте уважаемый преподаватель! Это программа учета тепловозов.\n')
    while choise != 0:
        choise = menu()
        if choise == 1:
            try:
                list = read()
                show(list)
                save(list)
            except:
                print('Список тепловозов пуст, сначала нужно добавить тепловоз в список!')
        elif choise == 2:
            try:
                list = read()
                std = ask(list)
                save(std)
            except:
                std = ask()
                save(std)
        elif choise == 3:
            try:
                list = read()
                std = dell(list)
                save(std)
            except:
                print('Выбранного вами тепловоза точно нет в списке!')
    input('Спасибо за использование нашего П.О. , нажмите Ентер чтобы выйти.')

main()