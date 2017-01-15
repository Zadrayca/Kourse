
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import PyQt5.QtWebEngineWidgets

class Browzer(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()

    def initUi(self):
        loadUi('mainwindow.ui', self)
        self.statusBar().showMessage('Приложение запущенно')




if __name__ == '__main__':
    app = QApplication(sys.argv)

    browzer = Browzer()
    browzer.show()

    sys.exit(app.exec_())
