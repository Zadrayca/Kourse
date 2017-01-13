import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QDoubleSpinBox,
    QVBoxLayout
)

class Course(QObject):
    def get(self):
        return 30.0

class CurrensyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initLayouts()
        self.initSignals()

    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)
        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        # self.convertBtn.setEnabled(False)

        self.convertBtn = QPushButton('Перевести', self)

    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClick)




    def initLayouts(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)

        self.setCentralWidget(self.w)


    def onClick(self):
        value = self.srcAmount.value()

        if value:
            self.resultAmount.setValue(value / Course().get())





if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrensyConverter()
    converter.show()

    sys.exit(app.exec_())



