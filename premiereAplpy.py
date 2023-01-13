
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGroupBox, QPushButton, QVBoxLayout, QRadioButton, QGridLayout, QCheckBox
from PySide6.QtCore import Slot

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excel to Word")
        self.resize(1280, 720)
        self.create_central_area()
        self.statusBar()
        

    def create_central_area(self):
        central_area = QWidget()
        gridLayout = QGridLayout(central_area)
        gridLayout.addWidget(self.create_files_groupbox(), 0, 0)
        gridLayout.addWidget(self.create_eng_fr_rbtn(), 0, 1)
        gridLayout.addWidget(self.create_format_rbtn(), 0, 2)

        self.setCentralWidget(central_area)


    def create_files_groupbox(self):
        gbox = QGroupBox("Choisir les fichiers à modifier:")
        vbox = QVBoxLayout()
        vbox.addWidget(QCheckBox("Exclusive choice 1"))
        vbox.addWidget(QCheckBox("Exclusive choice 2"))
        vbox.addWidget(QCheckBox("Exclusive choice 3"))
        vbox.addStretch(1)
        gbox.setLayout(vbox)
        return gbox

    def create_eng_fr_rbtn(self):
        gbox = QGroupBox("Choisir la langue:")
        vbox = QVBoxLayout()
        vbox.addWidget(QRadioButton("Anglais", checked = True))
        vbox.addWidget(QRadioButton("Francais"))
        vbox.addStretch(1)
        gbox.setLayout(vbox)
        return gbox

    def create_format_rbtn(self):
        gbox = QGroupBox("Choisir le format:")
        vbox = QVBoxLayout()
        vbox.addWidget(QRadioButton("Word", checked = True))
        vbox.addWidget(QRadioButton("PDF"))
        vbox.addStretch(1)
        gbox.setLayout(vbox)
        return gbox

    



    

        
    """label = QLabel("Choisir les fichiers à modifier:", central_area)
        label.setGeometry(50, 10, 270, 30)

        label2 = QLabel("Choisir les fichiers à modifier:", central_area)
        label2.setGeometry(500, 10, 270, 30)
        label2.setObjectName('test')

        btn = QPushButton('test', central_area)
        btn.setGeometry(500, 300, 270, 30)
    """


    @Slot()
    def buttonClicked(self):
        btn = self.sender()
        print("pierre")
            

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication()
    app.setStyleSheet(open('qss/Diffnes.qss').read())
    window= MainWindow()
    window.show()
    

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())