
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QToolButton, QGridLayout

from PyQt5.uic import loadUi

class Button(QToolButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.setMinimumSize(35, 35)



        self.setCheckable(True)



    # def on_click(self):
    #
    #     self.setDisabled(True)

        # if Button.click:
        #     Button.setDisabled(True)

    # def on_click(self):
    #
    #     Button.setDisabled(True)


    # def on_click(self):
    #     self.QToolButton.setCheckable(True)
    #     # if QToolButton.clicked:
    #     #     self.QToolButton.setDisabled(True)


class Saper(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.grid1()
        self.init_signals()
        # self.name[5].setDisabled(True)





    def init_ui(self):
        loadUi('KMainWindow.ui', self)

        #self.resize(370, 370)
        self.setMinimumSize(300, 340)
        self.setMaximumSize(300, 340)



    def init_signals(self):

        global q

        q = []

        for i in range(81):

            q.append(i)

        for i in q:

            # if self.name[i].triggered():
            #     self.name[i].setDisabled(True)

            self.name[i].clicked.connect(self.on_click)

        return q

    def on_click(self):
        pass

        # if self.name[3].clicked(bool):



        if self.click() == True:

            self.setDisabled(True)


    def grid1(self):

        self.grid = QGridLayout(self)

        self.centr.setLayout(self.grid)

        # button = self.toolButton

        self.name = []

        x = 0

        positions = [(i, j) for i in range(9) for j in range(9)]

        for position in positions:


            self.name.append('button' + str(x))

            #self.name = ('button' + str(x))



            self.name[x] = Button()




            self.grid.addWidget(self.name[x], *position)

            x += 1

        return self.name

        #self.name.button0.setDisabled(True)










if __name__ == '__main__':
    app = QApplication(sys.argv)

    saper = Saper()
    saper.show()

    sys.exit(app.exec_())
