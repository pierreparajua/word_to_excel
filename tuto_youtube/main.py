from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        button = QPushButton("press me")
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
