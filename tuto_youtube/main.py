
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QSlider
import sys

from mainwindow import MainWindow

app = QApplication(sys.argv)
widget = MainWindow(app)
widget.show()
app.exec()
