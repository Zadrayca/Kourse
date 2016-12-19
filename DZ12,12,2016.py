def arifmetic():
    print('Здравствуйте, это программа-калькулятор.')
    a, b, c = 0, 0, 0
    x = None
    try:
        while a == 0 or b == 0 or c == 0:
            a = int(input('Веедите первое значение:'))
            b = input('Введите математическую операцию:')
            c = int(input('Введите второе значение:'))
            if b == '+':
                x = a + c
            elif b == '-':
                x = a - c
            elif b == '*':
                x = a * c
            elif b == '/':
                x = a / c
            else:
                print('Неизвестная операция.')
    except:
        print('Неизвестная операция.')
    print('Результат :', x)


#arifmetic()

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
    else:
        return False

#print(is_year_leap(2000))

from math import sqrt
def square(stor):
    x = stor * 4
    y = stor * sqrt(2)
    z = stor ** 2
    return ('Периметр квадрата:', x, 'Диагональ квадрата:', y, 'Площадь квадрата:', z)

#print(square(5))


def season(month):
    if month in [12, 1, 2]:
        return 'Зима'
    elif month in [3, 4, 5]:
        return 'Весна'
    elif month in [6, 7, 8]:
        return 'Лето'
    elif month in [9, 10, 11]:
        return 'Осень'
    else :
        print('Неверный ввод.')

#print(season(10))


def bank(a, years):
    for i in range(years):
        a += a / 10
    return a

#print(bank(3000, 3))

def menu():
    """функция выводит меню, принимает выбор пользователя, и возвращает выбор"""
    choise = None
    while choise not in range(0, 6):
        try:
            choise = int(input('''\t\t\tЭто меню управления программой.
            Что-бы воспользоваться калькулятором выберете "1"
            Что-бы проверить, является ли год высокосным, выберете "2"
            Что-бы узнать периметр, диагональ и площадь квадрата, выберете "3"
            Что-бы узнать время года, выберете "4"
            Что-бы расчитать выгодность банковского вклада, выберете "5"
            Что-бы выйти из программы выберете "0"\n'''))
        except:
            continue
    return choise

def main():
    choise = None
    print('Здравствуйте, эта программа поможет вам расчитать некорорые математические задачки!')
    while choise != 0:
        choise = menu()
        if choise == 1:
            try:
                arifmetic()
            except:
                print('Ошибка!')
        elif choise == 2:
            try:
                print(is_year_leap(int(input('Введите год: '))))
            except:
                print('Ошибка!')
        elif choise == 3:
            try:
                print(square(int(input('Введите сторону квадрата: '))))
            except:
                print('Ошибка!')
        elif choise == 4:
            try:
                print(season(int(input('Введите номер месяца, что-бы узнать пору года: '))))
            except:
                print('Ошибка!')
        elif choise == 5:
            try:
                print(bank(int(input('Введите сумму банковского вклада:')), int(input('Введите введите продолжтельность вклада:'))))
            except:
                print('Ошибка!')
    input('Спасибо за использование нашего П.О. , нажмите Ентер чтобы выйти.')

main()