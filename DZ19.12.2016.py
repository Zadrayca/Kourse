#
#
#
# def paravoz(weels, lenght, height):
#     return weels, lenght, height
#
#
# def vagon(weels, lenght, height):
#     return weels, lenght, height

def count(funk):
    def new_funk(weels, lenght, height, ):
        pass




def pic(funk):
    def new_funk(weels, lenght, height, x):
        g = [['#'] * lenght for i in range(height)]
        for row in g:
            print(' '.join([str(elem) for elem in row]))
        print('O ' * weels)
        return funk(weels, lenght, height, x)
    return new_funk

x = 0

@pic
def paravoz(weels, lenght, height, x):
    return print('Паравоз №', x, '.', weels, 'колес,', lenght, 'длинна,', height, 'высота.')

#paravoz(5, 7, 3, x)

y = 0
@pic
def vagon(weels, lenght, height, y):
    return print('Вагон  №', y, '.', weels, 'колес,', lenght, 'длинна,', height, 'высота.')

#vagon(3, 5, 3, x)



def menu():
    """функция выводит меню, принимает выбор пользователя, и возвращает выбор"""
    choise = None
    while choise not in range(0, 3):
        try:
            choise = int(input('''\t\t\tЭто меню управления программой.
            Что-бы нарисовать новый паравоз, выберете "1"
            Что-бы нарисовать новый вагон, выберете "2"
            Что-бы выйти из программы выберете "0"\n'''))
        except:
            continue
    return choise


def main(x, y):
    choise = None
    print('Здравствуйте, эта программа нарисует для вас паравоз и вагоны.')
    while choise != 0:
        choise = menu()
        if choise == 1:
            try:
                x += 1
                paravoz(int(input('Введите кличество колес:')), int(input('Введите длинну:')), int(input('Введите высоту:')), x)
            except:
                print('Ошибка!')
        elif choise == 2:
            try:
                y += 1
                vagon(int(input('Введите кличество колес:')), int(input('Введите длинну:')), int(input('Введите высоту:')), y)
            except:
                print('Ошибка!')
    input('Спасибо за использование нашего П.О. , нажмите Ентер чтобы выйти.')

main(x, y)



