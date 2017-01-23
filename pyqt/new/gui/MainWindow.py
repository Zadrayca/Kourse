# coding: utf-8

from PyQt5.QtWidgets import QMainWindow

from .ui.Ui_Main_Window import Ui_MainWindow

from .NotesWidget import NotesWidget

from core.NoteModel import NoteModel



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

    def init_signals(self):
        self.actionAdd.triggered.connect(self.notesWidget.add_new_note)

        self.actionExit.triggered.connect(self.close)

        self.actionEdit.triggered.connect(self.notesWidget.edit_selected_note)

        self.actionRemove.triggered.connect(self.notesWidget.remove_selected_notes)

        self.notesWidget.selection_changed.connect(self.update_menu)

    def update_menu(self):
        selected = self.notesWidget.selected_rows()
        self.actionEdit.setEnabled(len(selected) == 1)
        self.actionRemove.setEnabled(bool(selected))

