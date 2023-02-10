
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QSlider
import sys

from widget import Widget

app = QApplication(sys.argv)
#app.setStyleSheet(open('../qss/style.qss').read())
widget = Widget()
widget.show()
app.exec()
