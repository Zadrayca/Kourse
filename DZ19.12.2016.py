#
#
#
# def paravoz(weels, lenght, height):
#     return weels, lenght, height
#
#
# def vagon(weels, lenght, height):
#     return weels, lenght, height


def pic(funk):
    def new_funk(weels, lenght, height, x):
        g = [['#'] * lenght for i in range(height)]
        for row in g:
            print(' '.join([str(elem) for elem in row]))
        print('O ' * weels)
        x += 1
        return funk(weels, lenght, height, x)
    return new_funk


x = 0
@pic
def paravoz(weels, lenght, height, x):

    return print('Паравоз №', x, '.', weels, 'колес,', lenght, 'длинна,', height, 'высота.')

paravoz(5, 7, 3, x)

#
# def vagon(weels, lenght, height):
#     return weels, lenght, height










        #
# q = [['#'] * 10 for i in range(5)]
# for row in q:
#     print(' '.join([str(elem) for elem in row]))