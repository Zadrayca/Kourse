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

        self.resize(300, 200)

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        # self.convertBtn.setEnabled(False)

        self.convertBtn = QPushButton('Перевести', self)
        self.cleanBtn = QPushButton('Очистить', self)

    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClick)
        self.cleanBtn.clicked.connect(self.onClean)
        self.srcAmount.valueChanged.connect(self.onVal)
        self.resultAmount.valueChanged.connect(self.onVal)


    def initLayouts(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        value = self.srcAmount.value() + self.resultAmount.value()
        self.convertBtn.setEnabled(bool(value))
        self.mainLayout.addWidget(self.cleanBtn)

        self.setCentralWidget(self.w)

    def onVal(self):
        value = self.srcAmount.value() + self.resultAmount.value()
        self.convertBtn.setEnabled(bool(value))





    def onClick(self):
        value = self.srcAmount.value()
        value2 = self.resultAmount.value()



        if value:
            self.resultAmount.setValue(value / Course().get())
            self.srcAmount.setValue(0.00)
        if value2:
            self.srcAmount.setValue(value2 * Course().get())
            self.resultAmount.setValue(0.00)



    def onClean(self):
        return self.srcAmount.setValue(0.00), self.resultAmount.setValue(0.00)

    def keyPressEvent(self, event):
        if event.key() == 16777221:
            self.onClick()







if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrensyConverter()
    converter.show()


    sys.exit(app.exec_())



