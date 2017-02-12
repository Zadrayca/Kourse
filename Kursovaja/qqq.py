
import sys, random

from PyQt5.QtCore import QTimer, pyqtSignal

from PyQt5.QtWidgets import QMainWindow, QApplication, QToolButton, QGridLayout, QPushButton, QLCDNumber, QSizePolicy

from PyQt5.uic import loadUi


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMinimumSize(30, 30)
        self.setMaximumSize(30, 30)

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

    def __init__(self, text, posit, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cellValue = text
        self.position = posit

    def open(self):
        self.setDisabled(True)
        self.setText(str(self.cellValue))
        self.shooted.emit(self.cellValue)




class Free(Button):
    miss = pyqtSignal()

    plase = [(i, j) for i in range(1, 11) for j in range(1, 11)]

    pl = []


    def __init__(self, posit, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.isOpened = False

        #self.cellValue = text
        self.position = posit
        self.pl.append(self.position)
        self.butt = []
        for i in range(100):
            self.butt.append('button' + str(i))
        m = [-1, 0, 1]
        self.find = [(i, j) for i in range(-1, 2) for j in m]
        self.find.pop(4)
        self.lfind = []
        # for i, j in self.find:
        #     a = self.position[0]; b = self.position[1]
        #     a += i; b += j
        #     self.lfind.append((a, b))
        # print(self.lfind[5])


    def open(self):
        if self.isOpened == False:
            self.setDisabled(True)
            self.setText(str())
            self.isOpened = True
            # Free(self.pl[5]).setDisabled(True)
            # if self.pl[5].isOpened == False:
            #      self.pl[5].open()
            # if self.pl[5].isOpened == False:
            #     Free(self.pl[5]).click()

            # if Free(self.pl[5]).isOpened == False:
            #     Free(self.pl[5]).isOpened = True

            #     Free(self.pl[5]).click()

        else:
            None


        #print(self.position)
        #for i in Free.pl:
        # if Free(self.pl[5]).isOpened == False:
        #     Free(self.pl[5]).isOpened = True
        #     print(Free(self.pl[5]).position)
        #
        #     Free(self.pl[5]).open()
        #
        # else:
        #     None

        # for i, j in self.find:
        #     #a = self.position[0]; b = self.position[1]
        #     a += i; b += j
        #     self.lfind.append((a, b))
        # for z in self.lfind:
        #     if z in self.pl:
        #         Free(z).open()







        #print(self.lfind)
        #self.miss.connect(self.alg)
        #a = self.position[0]; b = self.position[1]

    #def alg(self):
        # q = -1
        # for x, y in self.plase:
        #     q += 1
        #     a = self.position[0]; b = self.position[1]
        #     for w, e in self.find:
        #
        #         a -= w
        #         b -= e
        #         if x == a and y == b:
        #             Free(' ', (x, y)).open()         # Вот тут нифига не понимаю как вызвать открытие кнопки(((
        #         else:
        #             Plant(' ', (x, y)).open()        # Ну и тут соответственно


            #print(self.position)


    #def alg(self, position):



class Saper(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.grid1()
        self.init_signals()
        self.init_time()
        # self.count()

    def init_ui(self):
        loadUi('KMainWindow.ui', self)

        self.setMinimumSize(330, 400)
        self.setMaximumSize(330, 400)

    def lose_ui(self):
        loadUi('Loose.ui', self)
        self.exitButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.init_ui)
        self.okButton.clicked.connect(self.grid1)
        self.okButton.clicked.connect(self.init_time)

    def lose_bomb_ui(self):
        loadUi('Bomb.ui', self)
        self.timer.stop()
        self.exitButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.init_ui)
        self.okButton.clicked.connect(self.grid1)
        self.okButton.clicked.connect(self.init_time)


    def count(self):
        value = self.lcd.intValue()

        if not value:
            self.timer.stop()
            self.lose_ui()
        else:
            self.lcd.display(value - 1)


    def init_time(self):
        self.timer = QTimer()
        self.lcd.display(100)
        self.timer.timeout.connect(self.count)
        self.timer.start(1000)

    def init_signals(self):
        self.actionNew.triggered.connect(self.grid1)
        self.actionNew.triggered.connect(self.init_time)
        self.actionExit.triggered.connect(self.close)


    def on_click(self):
        pass

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
        c = -1

        bomb_l = []
        free_l = []
        plant_l = []
        for position, name in zip(self.plase, self.names):

            c += 1

            if name == 0:
                self.butt[c] = Free(position)
                free_l.append(c)
            elif position in self.bomb:
                self.butt[c] = Bomb()
                bomb_l.append(c)
            else:
                self.butt[c] = Plant(name, position)
                plant_l.append(c)

            self.grid.addWidget(self.butt[c], *position)

        for z in bomb_l:
            self.butt[z].clicked.connect(self.lose_bomb_ui)








if __name__ == '__main__':
    app = QApplication(sys.argv)

    saper = Saper()
    saper.show()

    sys.exit(app.exec_())
