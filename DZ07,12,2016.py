#encoding: utf-8
#нап функцию без аргументов кот принимает на вход имя, фамилию, возраст.
#запуск программы, в цикле работает эта функция.
#при закрытии программы сохрю список пользователей в файл.
#при новом запуске читаем список пользователей из файла, далее пункт2
#логируйте каждый запуск программы
#удаление пользователя

from datetime import datetime
import pickle
now = str(datetime.now())
sps = {}
def menu():
    """функция выводит меню, принимает выбор пользователя, и возвращает выбор"""
    choise = None
    while choise not in range(0, 5):
        try:
            choise = int(input('''\t\t\tЭто меню управления программой.
            Что-бы просмотреть список студентов выберете "1"
            Что-бы добавить студента в список выберете "2"
            Что-бы удалить студента из списка выберете "3"
            Что-бы выйти из программы выберете "0"\n'''))
        except:
            continue
    return choise
def ask(sps = None):
    if sps == None:
        sps = {}
        key = 1
        stud = input('Впишите данные студента через пробел:')
        sps[key] = stud
        return sps
    elif sps != None:
        x = sps.keys()
        y = []
        for i in x:
            y.append(i)
        y.sort()
        key = int(y[-1])
        stud = input('Впишите данные студента через пробел:')
        key += 1
        sps[key] = stud
        return sps
def dell(slist):
    key = int(input('Какого студента вы хотите удалить? введите номер:'))
    if key in slist:
        del slist[key]
        print('Студент', key, 'удален.')
    else:
        print('Выбранного вами студента нет в списке.')
    return slist
def save(slist):
    f = open('student.dat', 'wb')
    pickle.dump(slist, f)
    f.close()
def read():
    f = open('student.dat', 'rb')
    slist = pickle.load(f)
    return slist
def log():
    f = open('log.txt', 'a')
    f.write(now)
    f.write('\n')
    f.close()
def show(slist):
    for i in slist.items():
        print(i)
def main():
    log()
    choise = None
    print('\tЗдравствуйте уважаемый преподаватель! Это программа учета студентов.\n')
    while choise != 0:
        choise = menu()
        if choise == 1:
            try:
                list = read()
                show(list)
                save(list)
            except:
                print('Список студентов пуст, сначала нужно добавить студентов в список!')
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
                print('Выбранного вами студента точно нет в списке!')
    input('Спасибо за использование нашего П.О. , нажмите Ентер чтобы выйти.')

main()