# написать модуль check_disk.py
# - функция 1 получает на вход путь к директории
# считает размер суммы файлов
# в том числе с вложенными поддиректориями
# 2 - пробегает по указанной директории,
# находит все файлы с указанной подстрокой в имени
# в файле
#
#
#
#функция паравоз, вагон - принимает параметры, возвращает значения
#созд декораторы отрисовывающие паравоз и вагоны
#
#* декоратор счетчик запуска фунций. каждой функции отдельно.
#
#
#


def pic(funk):
    def new_funk(weels, lenght, height, x):
        g = [['#'] * lenght for i in range(height)]
        for row in g:
            print(' '.join([str(elem) for elem in row]))
        print('O ' * weels)
        x += 1
        return funk(weels, lenght, height, x)
    return new_funk



@pic
def paravoz(weels, lenght, height, x=0):
    weels = 10
    return print('Паравоз №', x, '.', weels, 'колес,', lenght, 'длинна,', height, 'высота.')

paravoz(5, 7, 3, 0)
