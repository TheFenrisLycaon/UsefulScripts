#! /home/fenris/Apps/anaconda3/envs/gui/bin/python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class ShadowBrowser(QMainWindow):

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Shadow Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Po")
        self.go_btn.setMaximumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMaximumHeight(30)

        self.forwd_btn = QPushButton(">")
        self.forwd_btn.setMaximumHeight(30)

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forwd_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(
            lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forwd_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://gogle.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)

        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = ShadowBrowser()
app.exec_()
