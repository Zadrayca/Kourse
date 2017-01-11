import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class LittleBig(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):
        self.resize(400, 300)

        self.setMinimumSize(300, 200)
        self.setMaximumSize(600, 400)

        self.btn = QPushButton('We will push the button!', self)
        self.setCentralWidget(self.btn)






if __name__ == '__main__':
    app = QApplication(sys.argv)

    start = LittleBig()
    start.show()

    sys.exit(app.exec_())  # код состояния


