
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QSlider
import sys

from widget import Widget

app = QApplication(sys.argv)
print(app)
widget = Widget()
widget.show()
app.exec()
