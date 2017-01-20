

from PyQt5.QtWidgets import QWidget

from .ui.Ui_Note_Edit_Dialog import Ui_Dialog


class NoteEditDialog(QWidget, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)