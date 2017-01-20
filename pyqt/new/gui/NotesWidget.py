

from PyQt5.QtWidgets import QWidget

from .ui.Ui_Notes_Widget import Ui_Form

from core.NoteModel import NoteModel

class NotesWidget(QWidget, Ui_Form):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_model(model)

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)

        self.notesView.setModel(self.__model)
        self.notesView.resizeColumnsToContents()


    def init_model(self, model):
        if isinstance(model, NoteModel):
            self.__model = model
            self.__model.select()
        else:
            raise RuntimeError('Переданная модель не NoteModel')