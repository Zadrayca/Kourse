
from PyQt5.QtCore import pyqtSignal, QDateTime


from PyQt5.QtWidgets import QDialog, QDataWidgetMapper

from .ui.Ui_Note_Edit_Dialog import Ui_Dialog


class NoteEditDialog(QDialog, Ui_Dialog):
    ready = pyqtSignal(bool, int, name='ready')

    def __init__(self, model, row=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.init_model(model)

        if row is None:
            # в режиме добавления
            self.__model.insertRow(self.__model.rowCount())
            self.__mapper.toLast()
        else:
            # работаем в режиме редактирования
            self.__mapper.setCurrentIndex(row)


    def init_ui(self):
        self.setupUi(self)

        self.plannedDateTimeEdit.setMinimumDate(QDateTime.currentDateTime().date())

        self.plannedDateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def init_model(self, model):
        self.__model = model

        self.__mapper = QDataWidgetMapper(self)
        self.__mapper.setModel(self.__model)

        self.__mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.__mapper.addMapping(self.titleEdit, 1)
        self.__mapper.addMapping(self.plannedDateTimeEdit, 2)
        self.__mapper.addMapping(self.contentEdit, 3)

    def accept(self): # это стандартный метод
        super().accept()
        self.__mapper.submit() # отправили данные в модель
        state = self.__model.submitAll() # отправить изменения в БД
        self.ready.emit(state, self.__mapper.currentIndex())

    def reject(self):
        super().reject()
        self.__mapper.revert() # отмена изменений
        self.__model.revertAll()

