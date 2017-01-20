# coding: utf-8

from PyQt5.QtWidgets import QMainWindow

#from PyQt5.uic import loadUi

from .ui.Ui_Main_Window import Ui_MainWindow

from .NotesWidget import NotesWidget

from core.NoteModel import NoteModel

#from .NotesEditDialog import NoteEditDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()
        self.init_signals()


    def init_ui(self):
        self.setupUi(self)

        self.notesWidget = NotesWidget(NoteModel(), self)
        self.stackedWidget.addWidget(self.notesWidget)
        self.stackedWidget.setCurrentWidget(self.notesWidget)

        # self.notesEditDialog = NoteEditDialog(self)
        # self.stackedWidget.addWidget(self.notesEditDialog)



        # loadUi('ui/main_window.ui', self)

    def init_signals(self):
        pass