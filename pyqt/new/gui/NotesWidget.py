

from PyQt5.QtWidgets import QWidget

from .ui.Ui_Notes_Widget import Ui_Form



class NotesWidget(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)