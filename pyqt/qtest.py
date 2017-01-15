import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QDoubleSpinBox,
    QVBoxLayout
)


class CurrensyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initLayouts()
        self.initSignals()

















if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrensyConverter()
    converter.show()

    sys.exit(app.exec_())

