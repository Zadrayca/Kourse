# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'note_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(497, 382)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(3, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.titleEdit = QtWidgets.QLineEdit(Dialog)
        self.titleEdit.setObjectName("titleEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.titleEdit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.plannedDateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.plannedDateTimeEdit.setObjectName("plannedDateTimeEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.plannedDateTimeEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.contentEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.contentEdit.setObjectName("contentEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.contentEdit)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новая заметка"))
        self.label_2.setText(_translate("Dialog", "Текст"))
        self.label_3.setText(_translate("Dialog", "Дата"))
        self.label.setText(_translate("Dialog", "Наименование"))

