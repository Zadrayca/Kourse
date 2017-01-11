import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class Start(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(400, 300)

        self.label = QLabel('Привет!!!', self)

        self.setCentralWidget(self.label)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    start = Start()
    start.show()

    sys.exit(app.exec_())  # код состояния


