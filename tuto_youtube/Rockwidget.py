from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget





class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")

        btn1 = QPushButton('btn1')
        btn1.clicked.connect(self.btn1_clicked)
        btn2 = QPushButton('btn2')
        btn2.clicked.connect(self.btn2_clicked)

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)

        self.setLayout(btn_layout)

    def btn1_clicked(self):
        print("btn1")

    def btn2_clicked(self):
        print("btn2")
