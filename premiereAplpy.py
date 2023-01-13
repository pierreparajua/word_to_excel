
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.resize(1280, 720)
        

        progressBar = QProgressBar(self)
        progressBar.setGeometry(10, 10, 300, 30)
        progressBar.setMaximum(100)
        progressBar.setValue(50)




if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication()
    window= MainWindow()
    window.show()
    

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())