
import sys, random

from PyQt5.QtCore import QTimer, pyqtSignal

from PyQt5.QtWidgets import QMainWindow, QApplication, QToolButton, QGridLayout, QPushButton, QLCDNumber, QSizePolicy

from PyQt5.uic import loadUi


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMinimumSize(35, 35)
        self.setMaximumSize(35, 35)
        # self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.setCheckable(True)

        self.clicked.connect(self.open)

    def open(self):
        raise NotImplementedError('Не реализовано!')


class Bomb(Button):
    wasted = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def open(self):
        self.setDisabled(True)
        self.setText('*')
        self.wasted.emit()


class Plant(Button):
    shooted = pyqtSignal(int)

    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cellValue = text

    def open(self):
        self.setDisabled(True)
        self.setText(str(self.cellValue))
        self.shooted.emit(self.cellValue)


class Saper(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.grid1()
        self.init_signals()
        # self.time()
        # self.count()






    def init_ui(self):
        loadUi('KMainWindow.ui', self)

        #self.resize(370, 370)
        self.setMinimumSize(330, 400)
        self.setMaximumSize(330, 400)


    # def count(self):
    #
    #
    #
    #
    #
    #
    # def time(self):
    #
    #     self.timer = QTimer()
    #
    #     #self.lcd.display(100)
    #
    #
    #
    #     # self.value = 1000
    #     # self.lcd.display(self.value)
    #     # self.value = self.value - 1
    #     #self.lcd.intValue()
    #
    #
    #     self.timer.timeout.connect(self.count)
    #
    #     self.timer.start(1000)
    #
    #
    #

    def init_signals(self):
        pass


        # # global q
        # #
        # # q = []
        # #
        # # for i in range(81):
        # #
        # #     q.append(i)
        # #
        # # for i in q:
        # #
        # #     # if self.name[i].triggered():
        # #     #     self.name[i].setDisabled(True)
        # #
        # #     self.name[i].clicked.connect(self.on_click)
        #
        # return q

    def on_click(self):
        pass

        # if self.name[3].clicked(bool):



        # if self.click() == True:
        #
        #     self.setDisabled(True)
        #


    def grid1(self):

        self.grid = self.gridLayout

        self.centr.setLayout(self.grid)





        q = 100
        b = 10

        m = [-1, 0, 1]

        find = [(i, j) for i in range(-1, 2) for j in m]

        print(find)

        self.butt = []
        self.bomb = []
        self.names = [0 for i in range(100)]

        self.plase = [(i, j) for i in range(1, 11) for j in range(1, 11)]
        print(self.plase)
        while len(self.bomb) != b:
            z = random.choice(self.plase)
            if z not in self.bomb:
                self.bomb.append(z)

        print(self.bomb)

        for i in range(q):
            self.butt.append('button' + str(i))
        # print(butt)
        # print(plase[99], butt[99])

        g = -1
        for x, y in self.plase:
            print('plase', x, y)
            g += 1

            for i, j in find:
                print('find', i, j)
                z = 0

                # if x == a and y == b:
                #     z += 1
                for a, b in self.bomb:
                    print('bomb', a, b)

                    r = None
                    t = None
                    r = x + i
                    t = y + j
                    print('x', x, 'y', y)
                    print('r', r, 't', t)
                    print('bomb', a, b)

                    if r == a and t == b:
                        z += 1
                self.names[g] += z

        print(self.names)
        print(len(self.names))
        c = 0
        for position, name in zip(self.plase, self.names):
            # if name == "0":
            #     name = 'B'

            self.butt[c] = Plant(name)

            self.grid.addWidget(self.butt[c], *position)

            for position, in zip(self.bomb):
                self.butt[c] = Bomb()

                self.grid.addWidget(self.butt[c], *position)

        # self.name = []
        #
        # x = 0
        #
        # positions = [(i, j) for i in range(10) for j in range(10)]
        #
        # for position in positions:
        #
        #     self.name.append('button' + str(x))
        #
        #     #self.name = ('button' + str(x))
        #
        #     self.name[x] = Button()
        #
        #
        #
        #
        #     self.grid.addWidget(self.name[x], *position)
        #
        #     x += 1
        #
        # return self.name
        #
        # #self.name.button0.setDisabled(True)










if __name__ == '__main__':
    app = QApplication(sys.argv)

    saper = Saper()
    saper.show()

    sys.exit(app.exec_())
