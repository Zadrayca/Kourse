
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QToolButton, QGridLayout

from PyQt5.uic import loadUi

class Button(QToolButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.setMinimumSize(35, 35)

        self.setCheckable(True)

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


    def init_ui(self):
        loadUi('KMainWindow.ui', self)

        #self.resize(370, 370)
        self.setMinimumSize(300, 340)
        self.setMaximumSize(300, 340)

    def init_signals(self):

        self.button.triggered.connect(self.close)

    def on_click(self):

        print(self.button)


    def grid1(self):

        grid = QGridLayout(self)

        self.centr.setLayout(grid)

        # button = self.toolButton



        positions = [(i, j) for i in range(9) for j in range(9)]

        for position in positions:
            self.button = Button()

            grid.addWidget(self.button, *position)










if __name__ == '__main__':
    app = QApplication(sys.argv)

    saper = Saper()
    saper.show()

    sys.exit(app.exec_())
