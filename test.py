
import sys

from PySide6.QtCore import Slot, QDir, QModelIndex, QPersistentModelIndex
from PySide6.QtGui import QIcon, QAction, QCloseEvent, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QComboBox, QCheckBox, QLabel, \
    QProgressBar, QSplitter, QTabWidget, QTreeView, QTextEdit, QTableView, QFileSystemModel, QWidget, QGroupBox, \
    QGridLayout, QRadioButton, QVBoxLayout, QScrollBar, QSpinBox, QSlider, QPushButton, QLineEdit, QLCDNumber


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test styles with PySide6/Qt")
        self.setWindowIcon(QIcon("icons/yes.png"))
        self.resize(1024, 500)

        self.createBars()
        self.createCentralArea()

    def createCentralArea(self):
        # Un QSplitter permet de diviser l'espace en sous-zones.
        # Un séparateur permet de contrôler l'espace alloué à chaque zone.
        splitter = QSplitter(Qt.Horizontal)

        # Un QTreeView permet d'afficher une arborescence.
        # Grâce au QFileSystemModel, on connecte le tree sur le disque dur.
        treeModel = QFileSystemModel()
        treeModel.setRootPath(QDir.currentPath())
        treeView = QTreeView()
        treeView.setModel(treeModel)
        treeView.expandToDepth(0)   # Ouverture du premier niveau

        # Un QTabWidget permet de définir des onglets
        tabWidget = QTabWidget(splitter)
        tabWidget.setTabPosition(QTabWidget.South)
        tabWidget.setMinimumWidth(300)
        tabWidget.addTab(treeView, "File System")
        tabWidget.addTab(QTreeView(), "Database")
        tabWidget.addTab(QTreeView(), "Help")

        # Un autre splitter pour séparer l'espace de droite du splitter principal 
        # en deux sous-zones affichées l'une sous l'autre (Qt.Vertical).
        verticalSplitter = QSplitter(Qt.Vertical, splitter)
        editor = QTextEdit(verticalSplitter)
        self.fillEditor(editor)
        propertyPanel = QWidget(verticalSplitter)
        gridLayout = QGridLayout(propertyPanel)
        gridLayout.addWidget(self.createFirstGroupBox(), 0, 0)
        group2 = QGroupBox("Second group")
        gridLayout.addWidget(self.createSecondGroupBox(), 0, 1)
        group3 = QGroupBox("Third group")
        gridLayout.addWidget(self.createThirdGroupBox(), 0, 2)

        # On définit le splitter principal comme étant le "Central Widget".
        self.setCentralWidget(splitter)

    def fillEditor(self, editor):
        # On charge le contenu du fichier dans l'éditeur
        with open("StyleDemo.py", "r") as file:
            content = "".join(file.readlines())
        editor.setText(content)

    def createFirstGroupBox(self):
        # On définit un premier groupe de cases à cocher (exclusives).
        group1 = QGroupBox("First group")
        vBox = QVBoxLayout()
        vBox.addWidget(QRadioButton("Exclusive choice 1", checked=True))
        vBox.addWidget(QRadioButton("Exclusive choice 2"))
        vBox.addWidget(QRadioButton("Exclusive choice 3"))
        vBox.addStretch(1)
        group1.setLayout(vBox)
        return group1

    def createSecondGroupBox(self):
        # On définit un second groupe de cases à cocher (non exclusives).
        group2 = QGroupBox("Second group")
        vBox = QVBoxLayout()
        vBox.addWidget(QCheckBox("Choice 1", checked=True))
        vBox.addWidget(QCheckBox("Choice 2", checked=True))
        vBox.addWidget(QCheckBox("Choice 3"))
        vBox.addStretch(1)
        group2.setLayout(vBox)
        return group2

    def createThirdGroupBox(self):
        # On définit un dernier groupe de widgets.
        group3 = QGroupBox("Third group")
        vBox = QVBoxLayout()
        vBox.addWidget(QSpinBox(value=50))
        vBox.addWidget(QSlider(Qt.Horizontal, value=50))
        vBox.addWidget(QPushButton("Click me"))
        vBox.addWidget(QLineEdit("Edit me"))
        vBox.addWidget(QLCDNumber(value=50))
        vBox.addStretch(1)
        group3.setLayout(vBox)
        return group3

    def createBars(self):
        # Définitions des actions : elles seront associées à la barre
        # de menu et aux différentes barres d'outils.
        actNew = QAction(QIcon("icons/new.png"), "&New", self)
        actNew.setShortcut("Ctrl+N")
        actNew.setStatusTip("New document")
        actNew.triggered.connect(self.new)

        actOpen = QAction(QIcon("icons/open.png"), "&Open...", self)
        actOpen.setShortcut("Ctrl+O")
        actOpen.setStatusTip("Open file")
        actOpen.triggered.connect(self.open)

        actSave = QAction(QIcon("icons/save.png"), "&Save", self)
        actSave.setShortcut("Ctrl+S")
        actSave.setStatusTip("Save File")

        actExit = QAction(QIcon("icons/exit.png"), "Exit", self)
        actExit.setShortcut("Alt+F4")
        actExit.setStatusTip("Exit")
        actExit.triggered.connect(self.close)

        actUndo = QAction(QIcon("icons/undo.png"), "&Undo", self)
        actUndo.setShortcut("Ctrl+Z")
        actUndo.setStatusTip("Undo")

        actRedo = QAction(QIcon("icons/redo.png"), "&Redo", self)
        actRedo.setShortcut("Ctrl+Y")
        actRedo.setStatusTip("Redo")

        actCopy = QAction(QIcon("icons/copy.png"), "&Copy", self)
        actCopy.setShortcut("Ctrl+C")
        actCopy.setStatusTip("Copy")

        actCut = QAction(QIcon("icons/cut.png"), "Cu&t", self)
        actCut.setShortcut("Ctrl+X")
        actCut.setStatusTip("Cut")

        actPaste = QAction(QIcon("icons/paste.png"), "&Paste", self)
        actPaste.setShortcut("Ctrl+V")
        actPaste.setStatusTip("Paste")

        actAbout = QAction(QIcon("icons/about.png"), "About...", self)
        actAbout.setStatusTip("About...")

        # Définition de la barre de menu
        menuBar = self.menuBar()

        file = menuBar.addMenu("&File")
        file.addAction(actNew)
        file.addSeparator()
        file.addAction(actOpen)
        file.addAction(actSave)
        file.addSeparator()
        file.addAction(actExit)

        edit = menuBar.addMenu("&Edit")
        edit.addAction(actUndo)
        edit.addAction(actRedo)
        edit.addSeparator()
        edit.addAction(actCopy)
        edit.addAction(actCut)
        edit.addAction(actPaste)

        help = menuBar.addMenu("&Help")
        help.addAction(actAbout)

        # Définition de trois barres d'outils
        toolbar = self.addToolBar("Standard ToolBar")
        toolbar.addAction(actNew)
        toolbar.addSeparator()
        toolbar.addAction(actOpen)
        toolbar.addAction(actSave)
        toolbar.addSeparator()
        toolbar.addAction(actExit)

        toolbar2 = self.addToolBar("Edit ToolBar")
        toolbar2.addAction(actUndo)
        toolbar2.addAction(actRedo)
        toolbar2.addSeparator()
        toolbar2.addAction(actCopy)
        toolbar2.addAction(actCut)
        toolbar2.addAction(actPaste)

        toolbar3 = self.addToolBar("Test ToolBar")
        comboBox = QComboBox(self)
        comboBox.addItems(["First item", "Second item", "Third item"])
        toolbar3.addWidget(comboBox)
        toolbar3.addSeparator()
        toolbar3.addWidget(QCheckBox("Check me", self))

        # Définition de la barre de statuts
        statusBar = self.statusBar()
        statusBar.showMessage("Theme/Stylesheet usage")

        progress = QProgressBar()
        progress.setMaximumHeight(18)
        progress.setValue(50)

        label = QLabel("Text position: 31,25")

        statusBar.addPermanentWidget(progress)
        statusBar.addPermanentWidget(label)

    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self, self.windowTitle(),
                                     "Are you sure to quit?",
                                     QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @Slot()
    def new(self):
        print("New document requested")

    @Slot()
    def open(self):
        filename, selectedFilter = QFileDialog.getOpenFileName(self, "Open file", ".")
        print(filename, selectedFilter)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())