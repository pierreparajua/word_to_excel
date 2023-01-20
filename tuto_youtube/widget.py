from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QPushButton, QMessageBox, QWidget, \
    QVBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")

        btn_hard = QPushButton("HARD")
        btn_hard.clicked.connect(self.button_clicked_hard)

        btn_critic = QPushButton("CRITIC")
        btn_critic.clicked.connect(self.button_clicked_critic)

        btn_inf = QPushButton("INF")
        btn_inf.clicked.connect(self.button_clicked_inf)

        # set layout
        layout = QVBoxLayout()
        layout.addWidget(btn_hard)
        layout.addWidget(btn_critic)
        layout.addWidget(btn_inf)
        self.setLayout(layout)

    def button_clicked_hard(self):
        sms = QMessageBox()
        sms.setMinimumSize(700, 200)
        sms.setWindowTitle("sms title")
        sms.setText("erreor hard")
        sms.setInformativeText("want do you want to do ? :")
        sms.setIcon(QMessageBox.Critical)
        sms.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        sms.setDefaultButton(QMessageBox.Ok)
        ret = sms.exec()
        if ret == QMessageBox.Ok:
            print("user ok")
        else:
            print("User cancel")

    def button_clicked_critic(self):
        sms = QMessageBox()
        sms.setMinimumSize(700, 200)
        sms.setWindowTitle("sms title")
        sms.setText("erreor hard")
        sms.setInformativeText("want do you want to do ? :")
        sms.setIcon(QMessageBox.Warning)
        sms.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        sms.setDefaultButton(QMessageBox.Ok)
        ret = sms.exec()
        if ret == QMessageBox.Ok:
            print("user ok")
        else:
            print("User cancel")

    def button_clicked_inf(self):
        print("info")
