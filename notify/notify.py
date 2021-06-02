import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QLabel, QMenu
import time
import guardian


class SystemTray(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("icon.png"), self)
        self.menu = QtWidgets.QMenu(self)
        self._quit_action = QAction("Quit", self)
        self._quit_action.triggered.connect(QApplication.quit)
        self.menu.addAction(self._quit_action)
        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()
        self.widget = Notification()
        geo = QApplication.primaryScreen().geometry()
        height = geo.height()
        width = geo.width()
        self.widget.setGeometry(width * 0.95, 0.025 * height, 100, 100)


class Notification(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.button = QtWidgets.QPushButton("x")
        self.button.clicked.connect(self.dismiss)
        self.button.resize(10, 10)
        self.text = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        layout_top = QtWidgets.QHBoxLayout()
        layout_top.addWidget(self.button, QtCore.Qt.AlignRight)
        self.layout.addLayout(layout_top)
        self.layout.addWidget(self.text)
        self.button.setFixedSize(25, 25)
        self.setStyleSheet("color: white; background-color: #343638;")
        self.articles = []
        self.next_button = QtWidgets.QPushButton("next")
        self.layout.addWidget(self.next_button)
        self.next_button.clicked.connect(self.next)
        QtCore.QTimer.singleShot(5000, self.notify)

    def next(self):
        self.articles.pop()
        self.articles.pop()
        self.articles.pop()
        self.articles.pop()
        self.articles.pop()
        self.articles.pop()
  

        self.text.setText(self.articles[len(self.articles) - 1].get_title())
        if len(self.articles) < 2:
            self.next_button.hide()

    def notify(self):
        articles = guardian.check_for_new()
        self.articles = articles
        if len(articles) > 0:
            self.text.setText(articles[len(articles) - 1].get_title())
            self.show()

    def dismiss(self):
        QtCore.QTimer.singleShot(5000, self.notify)
        self.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    if QtWidgets.QSystemTrayIcon.isSystemTrayAvailable():
        tray = SystemTray()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
