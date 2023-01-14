from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import  sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("test")

button = QPushButton()
button.setText("pierre")

window.setCentralWidget(button)

window.show()
app.exec()