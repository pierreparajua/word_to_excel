from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")
        # menuBar ans menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_action)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Cut")

        # toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)

        # status bar
        self.setStatusBar(QStatusBar(self))

        btn1 =QPushButton("bnt1")
        btn1.clicked.connect(self.btn1_clicked())
        self.setCentralWidget(btn1)




    def quit_action(self):
        self.app.quit()
    def btn1_clicked(self):
        print("btn1")
