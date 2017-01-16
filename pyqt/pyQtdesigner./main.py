
import sys
import stuff_rc

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi

try:
    from PyQt5.QtWebEngineWidgets import QWebEngineViev as QWebView
except ImportError:
    from PyQt5.QtWebKitWidgets import QWebView


class Browzer(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.init_signals()

    def initUi(self):
        loadUi('mainwindow.ui', self)

        self.webView = QWebView(self)
        self.mainLayout.addWidget(self.webView)
        self.init_history_buttons()



    def init_signals(self):
        self.actionAboutQt.triggered.connect(self.about_qt)

        self.backBtn.clicked.connect(self.webView.back)
        self.forwardBtn.clicked.connect(self.webView.forward)
        self.query.returnPressed.connect(self.on_enter_query)
        self.searchBtn.clicked.connect(self.on_enter_query)

        self.webView.urlChanged.connect(self.init_history_buttons)
        self.webView.urlChanged.connect(self.set_query)
        self.webView.titleChanged.connect(self.on_title_changed)
        self.webView.page().linkHovered.connect(self.on_link_hovered)

    def init_history_buttons(self):
        history = self.webView.page().history()

        self.backBtn.setEnabled(history.canGoBack())
        self.forwardBtn.setEnabled(history.canGoForward())

    def about_qt(self):
        QMessageBox.aboutQt(self, 'O Qt')


    def on_enter_query(self):
        url = QUrl.fromUserInput(self.query.text())
        self.webView.load(url)


    def on_title_changed(self, title):
        name = self.windowTitle().split(' | ').pop()
        self.setWindowTitle(title + ' | ' + name)

    def set_query(self, url):
        if isinstance(url, QUrl):
            self.query.setText(url.toString())

    def on_link_hovered(self, url, *args, **kwargs):
        self.statusBar().showMessage(url) # по идее url.toString()





if __name__ == '__main__':
    app = QApplication(sys.argv)

    browzer = Browzer()
    browzer.show()

    sys.exit(app.exec_())
