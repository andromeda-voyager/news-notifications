import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication
import guardian
import nyt


class SystemTrayItem(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.tray_icon = QtWidgets.QSystemTrayIcon(
            QtGui.QIcon("icon.png"), self)
        self.menu = QtWidgets.QMenu(self)
        self._quit_action = QAction("Quit", self)
        self._quit_action.triggered.connect(QApplication.quit)
        self.menu.addAction(self._quit_action)
        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()
        self.widget = Notification()


class Notification(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #343638;")
        self.setFixedSize(500, 100)
        geo = QApplication.primaryScreen().geometry()
        width = geo.width()
        self.setGeometry(width-self.width()-width*.005,
                         40, 500, 100)

        self.button_close = QtWidgets.QPushButton("X", self)
        self.button_close.clicked.connect(self.dismiss)
        self.button_close.setStyleSheet(
            "QPushButton:hover{font-weight: bold} QPushButton{border:none; padding:8px; color:white;}"
        )

        self.title = QtWidgets.QLabel("", self)
        self.title.setOpenExternalLinks(True)
        self.title.setStyleSheet("padding:10px")
        self.title.setWordWrap(True)

        self.button_next = QtWidgets.QPushButton("next", self)
        self.button_next.setStyleSheet(
            "QPushButton:hover{font-weight: bold} QPushButton{border:none; padding:10px; color:white;}"
        )

        self.button_next.clicked.connect(self.next)

        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.addWidget(
            self.button_next)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.button_close)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.top_layout)
        self.layout.addWidget(self.title)

        QtCore.QTimer.singleShot(1000, self.notify)

    def next(self):
        self.articles.pop()
        article = self.articles[len(self.articles)-1]
        self.title.setText("<a style=\"color:white;\" href=" + article.get_link() +
                           ">" + article.get_title() + "</a>")
        if len(self.articles) < 2:
            self.button_next.hide()

    def notify(self):
        articles = nyt.check_for_new()
        self.articles = articles
        if len(articles) > 0:
            article = articles[len(articles)-1]
            self.title.setText("<a style=\"color:white;\" href=" + article.get_link() +
                               ">" + article.get_title() + "</a>")
            self.show()

    def dismiss(self):
        QtCore.QTimer.singleShot(1000, self.notify)
        self.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    if QtWidgets.QSystemTrayIcon.isSystemTrayAvailable():
        tray = SystemTrayItem()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
